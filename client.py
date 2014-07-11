#!usr/bin/python3.4
import socket

sock = socket.socket()
sock.connect(('localhost', 1027))
sock.send('hello, world!')

data = sock.recv(1024)
sock.close()

print data