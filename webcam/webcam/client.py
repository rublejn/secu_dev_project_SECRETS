import time

import cv2
import numpy as np
import socket
import struct
from io import BytesIO

print('start client...')

# Capture frame
cap = cv2.VideoCapture(0)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('52.47.87.250', 5000))

while cap.isOpened():
    time.sleep(0.01)
    _, frame = cap.read()

    memfile = BytesIO()
    np.save(memfile, frame)
    memfile.seek(0)
    data = memfile.read()

    # Send form byte array: frame size + frame content
    client_socket.sendall(struct.pack("L", len(data)) + data)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
