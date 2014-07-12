#!usr/bin/python3.4
import socket
import pickle

sock = socket.socket()
sock.connect(('127.0.0.1', 1027))
while True:
    data = sock.recv(1024)
#   sock.close()
    s_data=pickle.loads(data)
    print (s_data)
sock.close()
input()