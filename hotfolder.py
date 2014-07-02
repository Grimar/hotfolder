#!usr/bin/python3.4
#TODO some important stuff

import os
import shutil
import sys
import multiprocessing as mp
import time
#import sched

folder = os.path.normpath("C:\\hotfolder")
if not os.path.exists(folder):
    os.mkdir(folder)

output = os.path.join(folder, 'output')
if not os.path.exists(output):
    os.mkdir(output)

q = mp.Queue()

threads = 4
thread_list=[]

def queue_add():
    for root, dirs, files in os.walk(folder):
        for dir in dirs:
            if not os.path.abspath(dir) == output:
                for file in files:
                    q.put(file)
                    print(file, 'added to queue')


def worker():
    print(q.get())


def worker_timer(t=10):
    while True:
        queue_add()
        worker()
        time.sleep(t)

if __name__ == "__main__":
    if threads >= 0:
        p = mp.Process(target=worker_timer)
        threads -= 1
        thread_list.append("worker_timer")
        p.start()
        p.join()