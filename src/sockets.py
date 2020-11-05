
def register_sockets(socketio):
    """
    Register all listeners for the sockets from the frontend.
    """
    @socketio.on('steering')
    def handle(data):
        print(f'Steering: {data}')

    @socketio.on('throttle')
    def handle(data):
        print(f'Throttle: {data}')