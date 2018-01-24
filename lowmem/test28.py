import os

keybackground28 = ['QQ', 'Weibo', 'Wechat', 'Templerun', 'Huihuideal', 'Youku', 'Taobao', 'Tingshu', 'Aqiyi',
                   'BaiduMap', 'Damai', 'Dianping', 'Didi', 'Didapinche', 'Todaynews', 'Jingdong', 'Gifmaker',
                   'Mojiweather', 'Qsbk', 'Soufun', 'Sogou', 'Wandoujia', 'Ximalaya', 'QQzone', 'facebook', 'Kugou',
                   'UC']
os.system("adb   install -r app-debug.apk")
os.system("adb   install -r app-debug-androidTest.apk")

def launchByUia(testname):
	os.system(
		"adb shell am instrument -w -r   -e debug false -e class com.spreadtrum.lowmemory.Background#" + testname + " com.spreadtrum.lowmemory.test/android.support.test.runner.AndroidJUnitRunner")

files = os.listdir(os.getcwd())
for apk in files:
	if apk.endswith('.apk'):
		os.system('adb  install -g ' + apk)
for testname in keybackground28:
	# print testname
	launchByUia(testname)