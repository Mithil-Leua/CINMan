import time
import socket

sock = socket.socket()
host = socket.gethostname()
port = 4567

sock.connect((host,port))