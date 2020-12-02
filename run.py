# under normal circumstances, this script would not be necessary. the
# sample_application would have its own setup.py and be properly installed;
# however since it is not bundled in the sdist package, we need some hacks
# to make it work

from flask_socketio import SocketIO

from src import create_app
from src.sockets import register_sockets

# create an app instance
app = create_app()
socketio = SocketIO(app, logging=True, ping_interval=0.5, ping_timeout=1.5)
register_sockets(socketio)
socketio.run(app, host='0.0.0.0', port=80)
