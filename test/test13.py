# coding:utf-8
import os
import re
import platform
import subprocess
#
# # 获取设备型号
# os.system('adb shell getprop ro.product.model >config.ini')
# # 获取系统android版本号
# os.system('adb shell getprop ro.build.version.release >> config.ini')
# # 获取cpu信息
# os.system('adb shell cat /proc/cpuinfo >> config.ini')
# # 获取屏幕分辨率
# os.system('adb shell wm size >> config.ini')
# # 获取内存信息
# os.system('adb shell cat /proc/meminfo >>config.ini')

# mt = (os.popen('adb  shell date +"%Y%m%d%H%M%S"')).read()
# testmt = re.split('\r\n', mt)[0]
#
# mttestcase = re.findall('\d+', testmt)[0]
# print mt + "  " + testmt + ' ' + mttestcase

system = platform.system()
if system is "Windows":
    find_util = "findstr"
else:
    find_util = "grep"


def get_focused_package_and_activity():
    system = platform.system()
    if system is "Windows":
        find_util = "findstr"
    else:
        find_util = "grep"
    if "ANDROID_HOME" in os.environ:
        if system == "Windows":
            command = os.path.join(os.environ["ANDROID_HOME"], "platform-tools", "adb.exe")
        else:
            command = os.path.join(os.environ["ANDROID_HOME"], "platform-tools", "adb")
    else:
        raise EnvironmentError(
            "Adb not found in $ANDROID_HOME path: %s." % os.environ["ANDROID_HOME"])
    cmd = "adb shell %s" % (" dumpsys activity | %s mFocusedActivity" % find_util)
    result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.read()
    pattern = re.compile(r"[a-zA-Z0-9\.]+/.[a-zA-Z0-9\.]+")
    return pattern.findall(result)[0]


#判断是否设置环境变量ANDROID_HOME


sleep_time = -1
dump_time = -1
while not 0 < sleep_time <= 10:
    try:
        sleep_time = float(raw_input("Please input sleep time(0-10s) :"))
    except:
        continue
while dump_time < 0:
    try:
        dump_time = int(raw_input("Please input dump times: "))
    except:
        continue

activity_name = get_focused_package_and_activity()
print "Current Activity: "
print activity_name

FRAME_LATENCY_CMD = "dumpsys SurfaceFlinger --latency"
results = os.popen('adb shell '+"{0} {1}".format(FRAME_LATENCY_CMD, activity_name))
result = subprocess.Popen(results, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readline()
print result