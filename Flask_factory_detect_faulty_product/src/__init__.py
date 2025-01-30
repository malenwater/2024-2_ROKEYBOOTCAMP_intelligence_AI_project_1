from flask import Flask
from flask_socketio import SocketIO
from dotenv import load_dotenv
import os
from src.routes import main_bp
from src.services.socket_events import setup_socket_events

def create_app():
    load_dotenv()
    
    app = Flask(__name__)
    
    # 환경 변수 설정
    app.config["ACCESS_KEY"] = os.getenv("ACCESS_KEY")
    app.config["URL"] = [os.getenv("URL_1"), os.getenv("URL_2")]
    

    socketio = SocketIO()
    app.register_blueprint(main_bp)
    # setup_socket_events(socketio)
    socketio.init_app(app)


    return app, socketio
