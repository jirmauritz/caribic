from src.controls.gps_control import gps_data
from flask_socketio import emit


def register_sockets(socketio):
    """
    Register all listeners for the sockets from the frontend.
    """
    from src.controls import esc
    from src.controls import servo

    @socketio.on('steering')
    def handle(direction):
        servo.steer(direction)

    @socketio.on('throttle')
    def handle(rate):
        esc.speed(rate)

    @socketio.on('disconnect')
    def handle():
        esc.speed(0)
        servo.steer(0)

    @socketio.on('location')
    def handle(l):
        tripple = gps_data()
        emit('location', tripple)


def register_sockets_test(socketio):
    """
    Register all listeners for the sockets from the frontend.
    """
    @socketio.on('steering')
    def handle(direction):
        print(f'Steering: {direction}')

    @socketio.on('throttle')
    def handle(rate):
        print(f'Throttle: {rate}')

    @socketio.on('disconnect')
    def handle():
        print('Disconnected')

    @socketio.on('connect')
    def handle():
        print('Connected')
