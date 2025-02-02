from src import create_app
from flask_socketio import SocketIO

# Flask 애플리케이션과 socketio 인스턴스를 반환
app, socketio = create_app()
"""_summary_
    간단한 superbai의 두 개의 URL과 superbai의 팀 키를 src/.env에 설정하고 사용하면 3개의 이미지인 원본, 1번 모델 이미지, 2번 모델 이미지와 
    그 결과를 아래 txt를 통해 확인 가능한 웹
"""

if __name__ == "__main__":
    # 모든 네트워크에서 접속 가능하도록 설정
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
