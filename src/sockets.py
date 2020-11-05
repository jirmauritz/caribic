from src.controls.servo import steer

def register_sockets(socketio):
    """
    Register all listeners for the sockets from the frontend.
    """
    @socketio.on('steering')
    def handle(direction):
        steer(direction)

    @socketio.on('throttle')
    def handle(data):
        print(f'Throttle: {data}')