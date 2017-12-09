# test3.py
# coding:utf-8

import os
import sys
import time
import re
import threading


def main():
    batteryinfo = os.popen('adb shell dumpsys battery')
    while True:
        batteryinf = batteryinfo.readline().strip()
        if batteryinf.startswith('level:') and batteryinf:
            battery = batteryinf.split(' ')[1]
            print battery
        elif not batteryinf:
            break
    if battery == 100:
        print 'f'


def getcurtime():
    curtime = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    return curtime


# main()
dev = 'SC98321E10078040340'
# curtime = '20171114190936'
# datetime = getcurtime()
# print datetime
# print os.makedirs('bugreport/' + dev + '_' + curtime)
# os.system('adb -s SC98321E10078040340 bugreport > ' + dev + '_' + curtime + '/' + str(datetime) + '.txt')
a = os.popen(
    'adb -s ' + dev + ' shell "getprop ro.build.description"').readline()
b = os.popen(
    'adb -s ' + dev + ' shell "getprop gsm.version.baseband"').readline()
c = os.popen(
    'adb -s ' + dev + ' shell "getprop gsm.version.baseband1"').readline()

print a + b + c

activitylist = open('D:/uninstall apk.ini', 'r')
print activitylist.readline()
activites = []
packs = []
while True:
    activity = activitylist.readline()
    if activity:
        packs.append(activity.split('/')[0])
        activites.append(activity)
    else:
        break

for item in packs:
    print 'pack:' + item
for item in activites:
    print 'activitys:' + item
