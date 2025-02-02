from flask import Blueprint, render_template, request, current_app
import asyncio
from src.services.api_client import call_two_models
from src.services.image_processing import draw_chip_Labeling1, draw_chip_Labeling2, check_chip_nomal
import base64 
from src.services.socket_events import setup_socket_events

main_bp = Blueprint('main', __name__)

image_data_list = []  # 업로드된 이미지 저장 리스트


@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/upload', methods=['POST'])
async def upload_file():
    if 'file' not in request.files:
        return "파일이 없습니다.", 400

    file = request.files['file']
    original_image_data = file.read()

    result1, result2 = await call_two_models(current_app.config["URL"], current_app.config["ACCESS_KEY"], original_image_data)
    score = 0.4
    
    labeling1_image_data = draw_chip_Labeling1(original_image_data, result1,score)
    labeling2_image_data = draw_chip_Labeling2(original_image_data, result2,score)
    # labeling2_image_data = draw_chip_Labeling2(original_image_data, result1)
    check_nomal = check_chip_nomal(result1,result2,score)
    
    image_data_list.insert(0, {
        'original': original_image_data,
        'grayscale': labeling1_image_data[0],
        'sepia': labeling2_image_data[0],
    })

    if len(image_data_list) > 3:
        image_data_list.pop()

    encoded_images = [
        {
            'original': base64.b64encode(img['original']).decode("utf-8"),
            'grayscale': base64.b64encode(img['grayscale']).decode("utf-8"),
            'sepia': base64.b64encode(img['sepia']).decode("utf-8"),
            "description_original": "<원본 이미지>\n" + check_nomal[0] + '\n' + check_nomal[1],
            "description_grayscale": "<칩 구성용품 디텍팅 이미지>\n" + labeling1_image_data[1],
            "description_sepia":  "<칩 불량 판정 이미지>\n" + labeling2_image_data[1]
        }
        for img in image_data_list
    ]
    
    socketio = current_app.extensions.get('socketio')  # 또는 Flask app 내에서 socketio 인스턴스를 가져올 방법
    emit_images = setup_socket_events(socketio)  # 이 부분이 중요!
    emit_images(encoded_images)
    
    return {"Meseesages": "upload suesses"}
