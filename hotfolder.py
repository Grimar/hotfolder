#!usr/bin/python3.4
#TODO some important stuff

import os
import shutil
import sys
import queue

folder = os.path.normpath("C:\\hotfolder")
if not os.path.exists(folder):
    os.mkdir(folder)

output = os.path.join(folder, 'output')
if not os.path.exists(output):
    os.mkdir(output)

q = queue.Queue()

threads = 4

print("EOL")
sys.exit(0)
