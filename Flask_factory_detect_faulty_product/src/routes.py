from flask import Blueprint, render_template, request, jsonify
from flask_socketio import SocketIO, emit
import os

# 블루프린트 생성
main_bp = Blueprint('main', __name__)

UPLOAD_FOLDER = './src/static/uploaded_images'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@main_bp.route('/')
def home():
    # 단순히 HTML 페이지를 렌더링, 세션 사용 안함
    return render_template('index.html')

@main_bp.route('/img_save', methods=["POST"])
def img_save():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file:
        # 파일 이름을 0000부터 9999까지 순차적으로 설정
        img_filename = f"{len(os.listdir(UPLOAD_FOLDER)) + 1 :04d}.jpg"
        img_path = os.path.join(UPLOAD_FOLDER, img_filename)
        
        try:
            file.save(img_path)
            
            # 실시간으로 클라이언트에 이미지 경로 전달
            print(img_path)
            print(img_path)
            print(img_path)
            emit('new_image', {'img_path': img_path}, broadcast=True)

            return jsonify({"message": "Image uploaded successfully"}), 200
        except Exception as e:
            return jsonify({"error": "Failed to save image"}), 500
    
    return jsonify({"error": "No image uploaded"}), 400

# WebSocket 이벤트 리스너
@main_bp.before_app_request
def handle_connect():
    print("A client connected!")

@main_bp.teardown_app_request
def handle_disconnect(exception=None):
    print("A client disconnected!")
