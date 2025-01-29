from src import create_app
from flask_cors import CORS

# Flask 애플리케이션과 socketio 인스턴스를 반환
app, socketio = create_app()
CORS(app)  # CORS 허용
if __name__ == "__main__":
    # 모든 네트워크에서 접속 가능하도록 설정
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
