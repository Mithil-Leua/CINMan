import time
import socket

#client side socket
#change the host , temporarily set to 10.6.15.113 
# host = address on which server is running.
sock = socket.socket()
host = "10.6.15.113"
port = 12345

sock.connect((host,port))

import cinmantest
sock.send(cinmantest.client_data.encode())
