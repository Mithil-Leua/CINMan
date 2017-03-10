import socket
import subprocess
import simplejson

sock = socket.socket()
host = socket.gethostname()
port = 6006

sock.connect((host,port))

filein = subprocess.call("who -m >tmpfile",shell = True,stdout = subprocess.PIPE)
file = open("tmpfile","r")
data = file.read()
data = data.split(" ")
file.close()

print("user id : " + data[0])

textmesg = input("Enter your message :")

while True :
	if textmesg == "" :
		textmesg = input("Please re-enter your message :")
	else :
		break

message = {"user" : data[0] , "message" : textmesg}
message = simplejson.dumps(message)
sock.send(message.encode())

filein = subprocess.call("rm tmpfile",shell = True)

