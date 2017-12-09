import os
import threading
import time
import datetime


def times():
    curtime = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    return curtime

print times()

# os.system('echo start  aiqiyi ' + times() + '>D:/time.txt')
# os.system(
#     "adb shell am instrument -w -r   -e debug false -e class com.spreadtrum.myapplication.uicase.Aiqiyi com.spreadtrum.myapplication.test/android.support.test.runner.AndroidJUnitRunner")
# os.system('echo start Backup ' + times() + '>D:/time.txt')
# os.system(
#     "adb shell am instrument -w -r   -e debug false -e class com.spreadtrum.myapplication.uicase.Backup com.spreadtrum.myapplication.test/android.support.test.runner.AndroidJUnitRunner")
# os.system('echo start  Baidu ' + times() + '>D:/time.txt')
# os.system(
#     "adb shell am instrument -w -r   -e debug false -e class com.spreadtrum.myapplication.uicase.Baidu com.spreadtrum.myapplication.test/android.support.test.runner.AndroidJUnitRunner")
# os.system('echo start BaiduMap ' + times() + '>D:/time.txt')
# os.system(
#     "adb shell am instrument -w -r   -e debug false -e class com.spreadtrum.myapplication.uicase.BaiDuMap com.spreadtrum.myapplication.test/android.support.test.runner.AndroidJUnitRunner")
# os.system('echo start  douyu ' + times() + '>D:/time.txt')
# os.system(
#     "adb shell am instrument -w -r   -e debug false -e class com.spreadtrum.myapplication.uicase.douyu com.spreadtrum.myapplication.test/android.support.test.runner.AndroidJUnitRunner")
# os.system('echo start  Fenghuang ' + times() + '>D:/time.txt')
# os.system(
#     "adb shell am instrument -w -r   -e debug false -e class com.spreadtrum.myapplication.uicase.FengHuang com.spreadtrum.myapplication.test/android.support.test.runner.AndroidJUnitRunner")
# os.system('echo start gaodemap ' + times() + '>D:/time.txt')
# os.system(
#     "adb shell am instrument -w -r   -e debug false -e class com.spreadtrum.myapplication.uicase.gaodemap com.spreadtrum.myapplication.test/android.support.test.runner.AndroidJUnitRunner")
# os.system('echo start huya ' + times() + '>D:/time.txt')
# os.system(
#     "adb shell am instrument -w -r   -e debug false -e class com.spreadtrum.myapplication.uicase.huya com.spreadtrum.myapplication.test/android.support.test.runner.AndroidJUnitRunner")
# os.system('echo start jingdong ' + times() + '>D:/time.txt')
# os.system(
#     "adb shell am instrument -w -r   -e debug false -e class com.spreadtrum.myapplication.uicase.jingdong com.spreadtrum.myapplication.test/android.support.test.runner.AndroidJUnitRunner")
# os.system('echo start kaixinxiaoxiaole  ' + times() + '>D:/time.txt')
# os.system(
#     "adb shell am instrument -w -r   -e debug false -e class com.spreadtrum.myapplication.uicase.kaixinxinxiaoxiaole com.spreadtrum.myapplication.test/android.support.test.runner.AndroidJUnitRunner")
# os.system('echo start panda ' + times() + '>D:/time.txt')
# os.system(
#     "adb shell am instrument -w -r   -e debug false -e class com.spreadtrum.myapplication.uicase.panda com.spreadtrum.myapplication.test/android.support.test.runner.AndroidJUnitRunner")
# os.system('echo start QQ ' + times() + '>D:/time.txt')
# os.system(
#     "adb shell am instrument -w -r   -e debug false -e class com.spreadtrum.myapplication.uicase.QQ com.spreadtrum.myapplication.test/android.support.test.runner.AndroidJUnitRunner")
# os.system('echo start subway ' + times() + '>D:/time.txt')
# os.system(
#     "adb shell am instrument -w -r   -e debug false -e class com.spreadtrum.myapplication.uicase.subway com.spreadtrum.myapplication.test/android.support.test.runner.AndroidJUnitRunner")
# os.system('echo start taobao ' + times() + '>D:/time.txt')
# os.system(
#     "adb shell am instrument -w -r   -e debug false -e class com.spreadtrum.myapplication.uicase.taobao com.spreadtrum.myapplication.test/android.support.test.runner.AndroidJUnitRunner")
# os.system('echo start templerun2 ' + times() + '>D:/time.txt')
# os.system(
#     "adb shell am instrument -w -r   -e debug false -e class com.spreadtrum.myapplication.uicase.templerun2 com.spreadtrum.myapplication.test/android.support.test.runner.AndroidJUnitRunner")
# os.system('echo start tencentvideo ' + times() + '>D:/time.txt')
# os.system(
#     "adb shell am instrument -w -r   -e debug false -e class com.spreadtrum.myapplication.uicase.Tencentvideo com.spreadtrum.myapplication.test/android.support.test.runner.AndroidJUnitRunner")
# os.system('echo start tmall ' + times() + '>D:/time.txt')
# os.system(
#     "adb shell am instrument -w -r   -e debug false -e class com.spreadtrum.myapplication.uicase.tmall com.spreadtrum.myapplication.test/android.support.test.runner.AndroidJUnitRunner")
# os.system('echo start TodayNews ' + times() + '>D:/time.txt')
# os.system(
#     "adb shell am instrument -w -r   -e debug false -e class com.spreadtrum.myapplication.uicase.TodayNews com.spreadtrum.myapplication.test/android.support.test.runner.AndroidJUnitRunner")
# os.system('echo start UC ' + times() + '>D:/time.txt')
# os.system(
#     "adb shell am instrument -w -r   -e debug false -e class com.spreadtrum.myapplication.uicase.UC com.spreadtrum.myapplication.test/android.support.test.runner.AndroidJUnitRunner")
# os.system('echo start Wechat ' + times() + '>D:/time.txt')
# os.system(
#     "adb shell am instrument -w -r   -e debug false -e class com.spreadtrum.myapplication.uicase.Wechat com.spreadtrum.myapplication.test/android.support.test.runner.AndroidJUnitRunner")
# os.system('echo start Weibo ' + times() + '>D:/time.txt')
# os.system(
#     "adb shell am instrument -w -r   -e debug false -e class com.spreadtrum.myapplication.uicase.Weibo com.spreadtrum.myapplication.test/android.support.test.runner.AndroidJUnitRunner")
# os.system('echo start Youku ' + times() + '>D:/time.txt')
# os.system(
#     "adb shell am instrument -w -r   -e debug false -e class com.spreadtrum.myapplication.uicase.Youku com.spreadtrum.myapplication.test/android.support.test.runner.AndroidJUnitRunner")
# os.system('echo end youku ' + times() + '>D:/time.txt')
