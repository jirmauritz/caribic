from flask_socketio import SocketIO

from src import create_app
from src.sockets import register_sockets_test

# create an app instance
app = create_app()
socketio = SocketIO(app, logging=True, ping_interval=0.5, ping_timeout=1.5)
register_sockets_test(socketio)
socketio.run(app, host='0.0.0.0', port=443, certfile='.secrets/yoga-15.local.crt', keyfile='.secrets/yoga-15.local.key')
