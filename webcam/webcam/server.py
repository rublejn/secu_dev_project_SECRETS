import time

from flask import Flask, render_template, Response
from streamer import Streamer

app = Flask(__name__)


def gen():
    while True:
        time.sleep(0.01)
        if streamer.streaming:
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + streamer.get_jpeg() + b'\r\n\r\n')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video_feed')
def video_feed():
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')


# @app.teardown_appcontext
# def close(exception):
#     streamer.stop()


if __name__ == '__main__':
    streamer = Streamer('0.0.0.0', 5000)
    streamer.start()
    app.run(host='0.0.0.0', port=800, threaded=True)
