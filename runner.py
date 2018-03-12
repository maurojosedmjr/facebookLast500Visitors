import sys
sys.path.insert(0, r'./libs/')

import os
dirFiles = r"./files/"
if not os.path.exists(dirFiles):
    os.mkdir(dirFiles)

dirLogs = r'./logs/'
if not os.path.exists(dirLogs):
    os.mkdir(dirLogs)

import checker as ck
import manipulate as mn

ck.runFindFriends()
mn.runManipulate()
