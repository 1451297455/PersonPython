import os

# kill = os.system("adb logcat | findstr died >>info.txt")
fil = os.popen("adb shell dumpsys meminfo ")
while True:
    line = fil.readline().strip()
    if line.startswith("Free RAM"):
        print line
    elif line.startswith("Tuning"):
        break
os.system("aiqiyi:")
os.system("adb shell dumpsys meminfo | findstr com.qiyi.video >>info.txt")
os.system("youku:")
os.system("adb shell dumpsys meminfo | com.youku.phone >>info.txt")

os.system("duoyu:")
os.system("adb shell dumpsys meminfo | findstr air.tv.douyu.android")

os.system("xiaoxiaole:")
os.system("adb shell dumpsys meminfo | findstr com.happyelements.AndroidAnimal.wdj >>info.txt")

os.system("wechat:")
os.system("adb shell dumpsys meminfo | findstr com.tencent.mm>>info.txt")
os.system("todaynews:")
os.system("adb shell dumpsys meminfo | findstr com.ss.android.article.news >>info.txt")

os.system("baidumap:")
os.system("adb shell dumpsys meminfo | findstr com.baidu.BaiduMap>>info.txt")

os.system("jingdong:")
os.system("adb shell dumpsys meminfo | findstr com.jingdong.app.mall >>info.txt")
os.system("tmall:")
os.system("adb shell dumpsys meminfo | findstr com.tmall.wireless >>info.txt")

os.system("moji:")
os.system("adb shell dumpsys meminfo | findstr com.moji.mjweather >>info.txt")

os.system("weibo:")
os.system("adb shell dumpsys meminfo | findstr com.sina.weibo>>info.txt")
os.system("subways:")
os.system("adb shell dumpsys meminfo | findstr com.kiloo.subwaysurf>>info.txt")

os.system("taobao:")
os.system("adb shell dumpsys meminfo | findstr com.taobao.taobao>>info.txt")

os.system("netcloud:")
os.system("adb shell dumpsys meminfo | findstr com.netease.cloudmusic>>info.txt")





