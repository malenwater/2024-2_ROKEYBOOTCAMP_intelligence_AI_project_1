from flask import Flask
from flask_socketio import SocketIO
from .routes import main_bp  # routes.py에서 블루프린트 import

# Flask 애플리케이션 초기화
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'JhG2K5utVR'

    # SocketIO 초기화
    socketio = SocketIO(app)

    # 블루프린트 등록
    app.register_blueprint(main_bp)

    return app, socketio
