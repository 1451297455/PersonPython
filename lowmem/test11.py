import os

keybackground11 = ['QQ', 'Wechat','Kugou', 'facebook', 'BaiduMap','Youku', 'Taobao', 'News', 'Sogou']
os.system("adb   install -r app-debug.apk")
os.system("adb   install -r app-debug-androidTest.apk")


def launchByUia(testname):
	os.system(
		"adb shell am instrument -w -r   -e debug false -e class com.spreadtrum.lowmemory.Background#" + testname + " com.spreadtrum.lowmemory.test/android.support.test.runner.AndroidJUnitRunner")

files = os.listdir(os.getcwd())
for apk in files:
	if apk.endswith('.apk'):
		os.system('adb  install -g ' + apk)
for testname in keybackground11:
	launchByUia(testname)