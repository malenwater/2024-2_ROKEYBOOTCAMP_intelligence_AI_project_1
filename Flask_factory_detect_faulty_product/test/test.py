from flask import Flask, render_template, request
from flask_socketio import SocketIO
from PIL import Image, ImageEnhance
import io
import base64
from requests.auth import HTTPBasicAuth
import cv2
import aiohttp
import asyncio
import numpy as np
import os
from dotenv import load_dotenv

app = Flask(__name__)
socketio = SocketIO(app)

# .env 파일 로드
load_dotenv()

# 환경 변수 불러오기
ACCESS_KEY = os.getenv("ACCESS_KEY")
URL = [os.getenv("URL_1"), os.getenv("URL_2")]

# 비동기 HTTP 요청 함수
async def solve_model(URL, ACCESS_KEY, image):
    async with aiohttp.ClientSession() as session:
        async with session.post(
            URL,
            auth=aiohttp.BasicAuth("kdt2025_1-22", ACCESS_KEY),
            headers={"Content-Type": "image/jpeg"},
            data=image
        ) as response:
            print(f"Request finished with status: {response.status}")
            return await response.json()

# 비동기로 두 개의 요청을 보내고, 결과가 올 때까지 기다리는 함수
async def call_two_models(URL, ACCESS_KEY, image):
    # 두 개의 요청을 동시에 보내고 결과가 오기를 기다림
    result1, result2 = await asyncio.gather(
        solve_model(URL[0], ACCESS_KEY, image),
        solve_model(URL[1], ACCESS_KEY, image)
    )
    return result1, result2

def draw_chip_Labeling1(image_bytes,response):
    item_color_map = {
        "RASPBERRY PICO": (255, 0, 0),    # 빨간색
        "HOLE": (0, 255, 0),             # 초록색
        "BOOTSEL": (0, 0, 255),          # 파란색
        "OSCILLATOR": (255, 255, 0),     # 노란색
        "USB": (0, 255, 255),            # 청록색
        "CHIPSET": (255, 0, 255)         # 보라색
    }
    class_confidence_text = ""
    image = np.frombuffer(image_bytes, dtype=np.uint8)  # 바이트 데이터를 numpy 배열로 변환
    img = cv2.imdecode(image, cv2.IMREAD_COLOR)  # 이미지를 디코딩하여 OpenCV 이미지 객체로 변환
    for one_data in response['objects']:
        # 이미지 파일 경로 설정
        # 박스 칠 좌표 설정 (예: 좌측 상단 (50, 50), 우측 하단 (200, 200))
        start_point = (one_data['box'][0], one_data['box'][1]) # 박스 시작 좌표 (x, y)
        end_point = (one_data['box'][2], one_data['box'][3]) # 박스 끝 좌표 (x, y)
        color = item_color_map[one_data['class']] # BGR 색상 (초록색)
        thickness = 2 # 박스 선의 두께
        # 박스 그리기
        cv2.rectangle(img, start_point, end_point, color, thickness)
        # 텍스트 설정
        class_confidence_text +=  one_data['class'] + " : "+ str(round(one_data['score'], 4)) + "\n"
        text = one_data['class'] + " : "+ str(one_data['score'])# 추가할 텍스트
        position = (one_data['box'][0] - 20, one_data['box'][1] - 10) # 텍스트 시작 위치 (x, y)
        font = cv2.FONT_HERSHEY_SIMPLEX # 글꼴 설정
        font_scale = 0.5 # 글자 크기
        color = item_color_map[one_data['class']] # BGR 색상 (초록색)
        thickness = 2 # 글자 두께
        # 텍스트 추가
        # cv2.putText(img, text, position, font, font_scale, color, thickness, cv2.LINE_AA)
        
    # 이미지 인코딩 (JPG 형식)
    ret, buffer = cv2.imencode('.jpg', img)
    if ret:
        return buffer.tobytes(), class_confidence_text  # ✅ **bytes로 변환하여 반환**
    else:
        raise ValueError("이미지 인코딩 실패")
    
def draw_chip_Labeling2(image_bytes,response):
    item_color_map = {
        "Broken": (255, 0, 0),    # 빨간색
        "Nomal": (0, 255, 0),             # 초록색
    }
    class_confidence_text = ""
    image = np.frombuffer(image_bytes, dtype=np.uint8)  # 바이트 데이터를 numpy 배열로 변환
    img = cv2.imdecode(image, cv2.IMREAD_COLOR)  # 이미지를 디코딩하여 OpenCV 이미지 객체로 변환
    for one_data in response['objects']:
        # 이미지 파일 경로 설정
        # 박스 칠 좌표 설정 (예: 좌측 상단 (50, 50), 우측 하단 (200, 200))
        start_point = (one_data['box'][0], one_data['box'][1]) # 박스 시작 좌표 (x, y)
        end_point = (one_data['box'][2], one_data['box'][3]) # 박스 끝 좌표 (x, y)
        color = item_color_map[one_data['class']] # BGR 색상 (초록색)
        thickness = 2 # 박스 선의 두께
        # 박스 그리기
        cv2.rectangle(img, start_point, end_point, color, thickness)
        # 텍스트 설정
        class_confidence_text +=  one_data['class'] + " : "+ str(round(one_data['score'], 4)) + "\n"
        text = one_data['class'] + " : "+ str(one_data['score'])# 추가할 텍스트
        position = (one_data['box'][0] - 20, one_data['box'][1] - 10) # 텍스트 시작 위치 (x, y)
        font = cv2.FONT_HERSHEY_SIMPLEX # 글꼴 설정
        font_scale = 0.5 # 글자 크기
        color = item_color_map[one_data['class']] # BGR 색상 (초록색)
        thickness = 2 # 글자 두께
        # 텍스트 추가
        # cv2.putText(img, text, position, font, font_scale, color, thickness, cv2.LINE_AA)
    print(class_confidence_text)
    print(class_confidence_text)
    print(class_confidence_text)
    # 이미지 인코딩 (JPG 형식)
    ret, buffer = cv2.imencode('.jpg', img)
    if ret:
        return buffer.tobytes(), class_confidence_text  # ✅ **bytes로 변환하여 반환**
    else:
        raise ValueError("이미지 인코딩 실패")
    
    
# 이미지를 저장할 리스트 (최대 9개)
image_data_list = []

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('upload_image')
def handle_upload():
    """클라이언트가 요청하면 현재 이미지 데이터를 전송"""
    if len(image_data_list) > 0:
        encoded_images = []
        for img in image_data_list:
            encoded_images.append({
                'original': base64.b64encode(img['original']).decode("utf-8"),
                'grayscale': base64.b64encode(img['grayscale']).decode("utf-8"),
                'sepia': base64.b64encode(img['sepia']).decode("utf-8")
            })
        socketio.emit('update_images', encoded_images)

@app.route('/upload', methods=['POST'])
async def upload_file():
    """파일 업로드 API"""
    global image_data_list
    if 'file' not in request.files:
        return "파일이 없습니다.", 400

    file = request.files['file']
    original_image_data = file.read()  # 원본 이미지 데이터 저장
    
    # print("jokoojojojojo", type(original_image_data))
    # # ------ 나중에 사라질 친구들, 아래 있는 데이터들은은
    # image = Image.open(io.BytesIO(original_image_data))  # 이미지 읽기
    # # --------------------------------------- 필없음
    # byte_io = io.BytesIO()
    # image.save(byte_io, format="JPEG")  # JPEG 형식으로 저장
    # byte_io.seek(0)  # BytesIO의 포인터를 처음으로 이동
    # image = byte_io.getvalue()  # image_bytes가 이제 바이트 데이터입니다
    # # --------------------------------------- 필없음
    result1, result2 = await call_two_models(URL, ACCESS_KEY, original_image_data)
    print("start")
    print(result1)
    print(result2)
    print("end")
    # 이미지를 회색조로 변환
    labeling1_image_data = draw_chip_Labeling1(original_image_data,result1)
    # 세피아 필터 적용
    labeling2_image_data = draw_chip_Labeling2(original_image_data,result2)

    # 원본 이미지, 회색조 이미지, 세피아 필터 이미지를 리스트에 저장
    image_data_list.insert(0, {
        'original': original_image_data,
        'grayscale': labeling1_image_data[0],
        'sepia': labeling2_image_data[0],
    })

    # 이미지가 9개 이상일 경우, 가장 오래된 이미지를 삭제
    if len(image_data_list) > 3:
        image_data_list.pop()  # 마지막 이미지 제거

    # 이미지를 base64로 인코딩하여 클라이언트로 전달
    encoded_images = []
    for img in image_data_list:
        encoded_images.append({
            'original': base64.b64encode(img['original']).decode("utf-8"),
            'grayscale': base64.b64encode(img['grayscale']).decode("utf-8"),
            'sepia': base64.b64encode(img['sepia']).decode("utf-8"),
            "description_original": "<원본 이미지>",
            "description_grayscale": "<칩 구성용품 디텍팅 이미지>\n" + labeling1_image_data[1],
            "description_sepia":  "<칩 불량 판정 이미지>\n" + labeling2_image_data[1]
        })

    socketio.emit('update_images', encoded_images)
    
    return "업로드 완료!", 200

if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
