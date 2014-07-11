#!usr/bin/python3.4

import os
import shutil
import sys
import multiprocessing as mp
import time
import socket
#import sched

folder = os.path.normpath("C:\\hotfolder")
if not os.path.exists(folder):
    os.mkdir(folder)

output = os.path.join(folder, 'output')
if not os.path.exists(output):
    os.mkdir(output)

q = []

threads = 4
thread_list=[]

def queue_add():
    for root, dirs, files in os.walk(folder):
        for dir in dirs:
            if not os.path.abspath(dir) == output:
                for file in files:
                    q.append(file)
                    print(file, 'added to queue')


def worker(command=''):
    print(q[-1:])


def worker_timer(t=10):
    while True:
        queue_add()
        worker()
        time.sleep(t)

def conn(port=1027):
    sock=socket.socket()
    sock.bind(('',port))
    sock.listen(5)
    print('Listening on port', port)
    conn, addr = sock.accept()
    print('Connected: on port', addr)
    conn.send(b'You connected to me!')


if __name__ == "__main__":
    if threads >= 0:
        p = mp.Process(target=worker_timer)
        threads -= 1
        thread_list.append("worker_timer")
        p.start()
    if threads >=0:
        c = mp.Process(target=conn)
        threads -= 1
        thread_list.append("conn")
        c.start()

        p.join()
        c.join()