import os

hf_input = []


class Input():

    def __init__(self, name):
        self.name = name
        self.path = os.path.abspath(self.name)
        self.size = os.path.getsize(self.name)

    def __sizeof__(self):
        pass

