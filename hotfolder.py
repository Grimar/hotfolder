#!usr/bin/python3.4

import os
import shutil
import sys
import multiprocessing as mp
import time
import socket
import pickle
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

def conn(thread_list, q, port=1027, timeout=5):
    sock=socket.socket()
    sock.bind(('',port))
    sock.listen(5)
    print('Listening on port', port)
    conn, addr = sock.accept()
    print('Connected: on address', addr)
#   conn.send(data)
    while conn:
        conn.send(pickle.dumps([thread_list, q]))
        time.sleep(timeout)
    conn.close()



if __name__ == "__main__":
    if threads >= 2:
        threads -= 1
        thread_list.append("worker_timer")
        p = mp.Process(target=worker_timer)
        p.start()
        threads -= 1
        thread_list.append("conn")
        c = mp.Process(target=conn(thread_list, q))
        c.start()
