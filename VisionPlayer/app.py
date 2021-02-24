from flask import *
from flask_socketio import SocketIO
from blueprints import play
from sockets import comment

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'
socketio = SocketIO(app)
@app.route('/')
def index():
    return redirect(url_for("play.index"))

app.register_blueprint(play.bp)


comment.register_comment(socketio)

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=80, debug=True, threaded='True')
    socketio.run(app, host='0.0.0.0', port=888, debug=True)
