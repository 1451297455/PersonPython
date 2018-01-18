# coding:utf-8
import os
import threading
import time
import sys
# import multiprocessing
from untils import until as un

# devices 数组
devlist = []
# 线程池
threadpool = []
# 共享盘资源路径

sharePath = "//10.29.1.11\\DeptShared\\Test\\Beta_Group" + u"\\06性能测试PerformanceTest\\00PerformanceApk\\测试资源\\低内存测试apk"
sharePath1 = "//10.29.1.11\\DeptShared\\Test\\Beta_Group" + u"\\06性能测试PerformanceTest\\00PerformanceApk\\测试资源\\关键性能预置条件v1.2\\Native\关键性能Apk"
sharePath2 = "//10.29.1.11\\DeptShared\\Test\\Beta_Group" + u"\\14临时文件" + "\\00_jinchao.zhang\\Debug\\lowmem\\apk"
desFilename = sys.path[0] + '\\apk\\'
# QQ同步助手下载地址
link = 'http://mmgr.myapp.com/msoft/sec/secure/GodDresser/11/2/3/102021/qqpim_6.7.8.2080_android_20171205115928_main_release_20171205162055_102021.apk'
# 关键性能 11后台
keybackground11 = ['QQ', 'Wechat', 'Weibo', 'Kugou', 'facebook', 'BaiduMap', 'UC', 'Youku', 'Taobao', 'News', 'Sogou']
# 关键性能 28后台
keybackground28 = ['QQ', 'Weibo', 'Wechat', 'Templerun', 'Huihuideal', 'Youku', 'Taobao', 'Tingshu', 'Aqiyi',
                   'BaiduMap', 'Damai', 'Dianping', 'Didi', 'Didapinche', 'Todaynews', 'Jingdong', 'Gifmaker',
                   'Mojiweather', 'Qsbk', 'Soufun', 'Sogou', 'Wandoujia', 'Ximalaya', 'QQzone', 'facebook', 'Kugou',
                   'UC']
# 低内存 512M后台
Lowmem512 = ['QQ', 'Weibo', 'Wechat', 'facebook', 'Templerun', 'Sunwaysurfer', 'Happyelements', 'Huihuideal', 'Taobao',
             'Youku', 'YY', 'Aqiyi', 'Sogou', 'Neteasenews', 'Todaynews', 'BaiduMap', 'Didi', 'Didapinche', 'Ximalaya',
             'QQzone', 'QQmusic', 'UC', 'Baiduweb', 'Wandoujia']
# 低内存 1G后台
Lowmem1G = ['QQ', 'Weibo', 'Wechat', 'facebook', 'Templerun', 'Sunwaysurfer', 'Happyelements', 'Huihuideal', 'Taobao',
            'Youku', 'YY', 'Aqiyi', 'Damai', 'Didapinche', 'Eleme', 'Neteasenews', 'Todaynews', 'BaiduMap', 'Didi',
            'Didapinche', 'Tingshu', 'Gifmaker', 'Mojiweather', 'Qsbk', 'Soufun', 'Sogou', 'Wandoujia', 'Ximalaya',
            'QQzone', 'QQmusic', 'UC', 'Baiduweb']
# 低内存 2G后台
Lowmem2G = ['QQ', 'Weibo', 'Wechat', 'facebook', 'Messenger', 'Templerun', 'Sunwaysurfer', 'Happyelements', 'Fish2',
            'Fish3', 'Bigeye', 'Huihuideal', 'Taobao', 'YY', 'Tingshu', 'Tmall', 'Jingdong', 'Aqiyi', 'Youku', 'Letv',
            'Bilibili', 'Souhutv', 'BaiduMap', 'Didi', 'Didapinche', 'Todaynews', 'Zhihu', 'News', 'Neteasenews',
            'Damai', 'Dianping', 'Eleme', 'Mojiweather', 'Soufun', 'Ecalendar', 'Netdisk', 'QQpimsecure', 'Sogou',
            'Wandoujia', 'Stock', 'CCB', 'Wps', 'Kuwo', 'Meipaimv', 'Gifmaker', 'Qsbk', 'Ximalaya', 'QQzone', 'QQmusic',
            'UC', 'Baiduweb', 'Joke']
# 低内存 3G后台
Lowmem3G = []

back = []


def pre(dev, back1, tel):
	background = back1
	# 打开wifi 8.0及以上能用  7.0命令无效
	os.system("apk\case\AndroidAdb.exe -s " + dev + " shell  svc wifi disable ")
	# 下载qq同步助手.apk
	un.down(link, "apk/case", dev)

	# 执行同步操作case 初始化本地应用
	print "同步联系人case 初始化本地应用".decode('utf-8')
	os.system("apk\case\AndroidAdb.exe -s " + dev + " install -r apk/case/app-debug.apk")
	os.system("apk\case\AndroidAdb.exe -s " + dev + " install -r apk/case/app-debug-androidTest.apk")
	os.system("apk\case\AndroidAdb.exe -s " + dev + " shell  svc data enable ")
	os.system("apk\case\AndroidAdb.exe -s " + dev + " shell  svc data prefer ")
	os.system(
		"apk\case\AndroidAdb.exe -s " + dev + " shell am instrument -w -r   -e debug false -e class com.spreadtrum.lowmemory.QQsync com.spreadtrum.lowmemory.test/android.support.test.runner.AndroidJUnitRunner")
	# 打开wifi
	os.system("apk\case\AndroidAdb.exe -s " + dev + " shell  svc wifi enable ")
	os.system("apk\case\AndroidAdb.exe -s " + dev + " shell  svc data disable ")
	# 获取共享盘资源——apk资源
	if background == 'Lowmem512':
		soucepath = sharePath + u'\\512MB-低内存'
	elif background == 'Lowmem1G':
		soucepath = sharePath + u'\\1G-低内存'
	elif background == 'Lowmem2G':
		soucepath = sharePath + u'\\2G-低内存'
	elif background == 'Lowmem3G':
		soucepath = sharePath + u'\\3G-低内存'
	elif background == '11':
		soucepath = sharePath1 + u'\\11后台'
	elif background == '28':
		soucepath = sharePath1 + u'\\28后台'

	if background == '0':
		pass
	else:
		un.getdirs(soucepath, desFilename + background)

	# 安装后台apk
	lists = un.install(background, dev)
	os.system('rd /s /q ' + desFilename + background)

	# 关键性能不需要重启
	if background == '11' or background == '0' or background == '28':
		pass
	else:
		# 重启等5min
		os.system("apk\case\AndroidAdb.exe -s " + dev + " reboot")
	time.sleep(10)
	os.system('apk\case\AndroidAdb.exe wait-for-devices')
	time.sleep(300)

	# 启动后台
	if background == '11':
		back = keybackground11
	elif background == '28':
		back = keybackground28
	elif background == '0':
		back = ['ss']
	elif background == 'Lowmem512':
		back = Lowmem512
	elif background == 'Lowmem1G':
		back = Lowmem1G
	elif background == 'Lowmem2G':
		back = Lowmem2G
	elif background == 'Lowmem3G':
		back = Lowmem3G

	# 启后台
	for testname in back:
		un.launchByUia(testname, dev)

	# un.launch(lists, dev)
	# 卸载case apk
	os.system("apk\case\AndroidAdb.exe -s " + dev + " uninstall com.spreadtrum.lowmemory.test")
	# 完成后电话通知
	os.system(
		"apk\case\AndroidAdb.exe -s " + dev + " shell am start -a android.intent.action.CALL -d tel:" + str(tel))


# 等待工具下载完成
# tag = False
# while not tag:
# 	tag = un.getdirs(sharePath2, desFilename + 'case')

# 等待device连接
print 'wait for device'
os.system('apk\case\AndroidAdb.exe wait-for-devices')

# 定义安装后台数
background = ""

while True:
	case = input('please input 1 or 2 (1:low memory   2:key performance):')
	if case == 1 or case == 2:
		break

while True:
	if case == 1:
		mem = input('please input meminfo 0,1,2 or 3 (0:512MB  1:1G  2:2G  3:3G):')
		if mem == 0 or mem == 1 or mem == 2:
			if mem == 0:
				background = 'Lowmem512'
			elif mem == 1:
				background = 'Lowmem1G'
			elif mem == 2:
				background = 'Lowmem2G'
			elif mem == 3:
				background = 'Lowmem3G'
			break
	if case == 2:
		background = raw_input('please input 0,11 or 28 :')
		if (background == '0' or background == '11' or background == '28'):
			break

tel = input('input tel :')
if not tel > 0:
	tel = 1

print '开始同步数据 ........'.decode('utf-8')

# 获取devices
devices = os.popen('apk\case\AndroidAdb.exe devices')
while True:
	dev = devices.readline().strip()
	if dev and dev.endswith('device'):
		devlist.append(dev.split()[0])
	elif dev and not dev.endswith('device'):
		continue
	elif not dev:
		break

for devs in devlist:
	vh = threading.Thread(target=pre, args=(devs, background, tel))
	vh.setDaemon(True)
	vh.start()
	vh.join()

'''# 实现多线程同步执行 出现资源抢占问题 待解决

n = len(devlist)
i = 0
while True:
	if i < n:
		vh = threading.Thread(target=pre, args=(devlist[i], background, tel))
		threadpool.append(vh)
		threadpool[i].setDaemon(True)
		threadpool[i].start()
		i = i + 1

m = 0
while True:
	if m < n:
		threadpool[m].join()
		m = m + 1
	else:
		break
'''

raw_input("Press <enter>")
