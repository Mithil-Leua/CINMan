import socket 
import time

MAXBUFFER = 1024

host = socket.gethostname()
port = 6006

s = socket.socket()
s.bind((host,port))

s.listen(5)

print("server started")

while True:
	try : 
		c , addr = s.accept()
		data = c.recv(MAXBUFFER).decode("ascii")
		print(str(addr) + " : " + data)
	except :
		break 

