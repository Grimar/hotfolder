#!usr/bin/python3.4
import socket

sock = socket.socket()
sock.connect(('127.0.0.1', 1027))
data = sock.recv(1024)
#    sock.close()
print (data.decode('UTF-8'))
sock.close()
input()