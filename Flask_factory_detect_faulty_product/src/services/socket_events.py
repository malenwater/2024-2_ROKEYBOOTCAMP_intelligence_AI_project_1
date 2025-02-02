from flask_socketio import emit

# 이벤트 처리 함수 설정
def setup_socket_events(socketio):
    @socketio.on('connect')
    def handle_connect():
        print("Client connected.")

    @socketio.on('disconnect')
    def handle_disconnect():
        print("Client disconnected.")

    # 다른 이벤트들 추가 가능
    # 예: `socketio.on('some_event')` 방식으로 처리
    @socketio.on('update_images')  # 클라이언트로부터 받는 이벤트 이름
    def handle_update_images(data):
        print("Received data:", data)  # 받은 데이터를 출력

    # 추가적으로 socketio.emit()을 통한 서버에서 클라이언트로 메시지를 보내는 부분 추가
    def emit_images(encoded_images):
        socketio.emit('update_images', encoded_images)  # 기본 네임스페이스 '/'로 지정
    return emit_images