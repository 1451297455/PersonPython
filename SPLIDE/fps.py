import os
import time
import re


def getfps(dev):
    stra = os.popen("adb -s " + dev + " shell dumpsys SurfaceFlinger | findstr flips", 'r')
    items = stra.readline().strip().split(',')
    for item in items:
        if item.strip().startswith('flips'):
            fps = item.split('=')[1]
            return int(fps)


def fps(dev):
    while True:
        start = time.time()
        fps1 = getfps(dev)
        time.sleep(1)
        fps2 = getfps(dev)
        end = time.time()
        print 'time:' + str(end - start - 0.3) + '  fps:' + str(
            int((fps2 - fps1) / (end - start - 0.3)))


os.system('adb wait-for-device')
devices = os.popen('adb devices')
devlist = devices.readline()
try:
    dev1 = devices.readline().split()[0]
    dev2 = devices.readline().split()[0]
except IndexError:
    dev2 = ''
    if len(dev2) == 1 and len(dev1) > 1:
        fps(dev1)
    elif len(dev2) > 1:
        print '1:' + dev1 + '\n' + '2:' + dev2
        num = input("input device num:")
        num = str(num) + "1"
        if num == '11':
            fps(dev1)
        elif num == '21':
            fps(dev2)
        else:
            pass
    elif len(dev1) == 1:
        print 'no devices'

