import os
import sched
import time as t

hf_input = []
folders = []

class Input():

    def __init__(self, name):
        self.name = name

        self.path = os.path.abspath(self.name)
        self.size = os.path.getsize(self.name)

    def __sizeof__(self):
        pass


class Queue():

    def __init__(self):
        pass

    def __getitem__(self, item):
        pass

    def append(self, obj):
        pass


class Folder():

    def __init__(self, path, name = "untitled", time = 10, queue = [Queue()]):
        self.name = name
        self.path = path
        self.time = time
        self.queue = queue

    def timer(self):
        for folder in self.queue:
            s = sched.scheduler(t.time, t.sleep)
            s.enter(self.time, 1, )
            s.run()



class Executor():

    def __init__(self):
        pass

