from src.controls import servo

def register_sockets(socketio):
    """
    Register all listeners for the sockets from the frontend.
    """
    @socketio.on('steering')
    def handle(direction):
        servo.steer(direction)

    @socketio.on('throttle')
    def handle(data):
        print(f'Throttle: {data}')
