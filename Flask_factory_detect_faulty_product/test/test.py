from flask import Flask, request, render_template, send_file
import io

app = Flask(__name__)

# 이미지 데이터를 저장할 변수 (메모리 저장 방식)
image_data = None

@app.route('/')
def index():
    return render_template('index.html', image_url="/receive_image")

@app.route('/upload', methods=['POST'])
def upload_file():
    global image_data  # 전역 변수 사용
    if 'file' not in request.files:
        return "파일이 없습니다.", 400

    file = request.files['file']
    image_data = file.read()  # 이미지 데이터 저장
    return "업로드 완료!", 200

@app.route('/receive_image')
def receive_image():
    if image_data is None:
        return "이미지가 없습니다.", 404
    
    return send_file(io.BytesIO(image_data), mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True)
