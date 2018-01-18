# coding:utf-8
import os
import time
import subprocess

adb = os.getcwd() + '/tool/adb.exe'


# 获取安装apk的包名和activity名
def getpackage(apk):
	lable = ''
	activname = ''
	packname = ''
	infos = os.popen(os.getcwd() + "/tools/aapt.exe dump badging apklist/" + apk)
	while True:
		info = infos.readline().strip()
		if info:
			if info.startswith("package:"):
				packname = info.split('\'')[1]
				continue
			elif info.startswith('application-label:'):
				lable = apk.split('.apk')[0]
				continue
			elif info.startswith('launchable-activity'):
				activname = info.split('\'')[1]
				break
		else:
			break
	return packname + '/' + activname, lable


# kill抓取log 进程
def killlogcat(dev):
	version = os.popen('adb  -s ' + dev + ' shell getprop | findstr version.release')
	pslogcat = version.readline().strip()
	if '[8' in pslogcat:
		result = os.popen('adb  -s ' + dev + ' shell ps -All | findstr logcat')
		while True:
			log = result.readline().strip()
			if log and 'logcat' in log:
				os.system("adb -s " + dev + " shell kill " + log.split()[3])
			if log and not 'logcat' in log:
				continue
			if not log:
				break
	else:
		result = os.popen('adb -s ' + dev + ' shell ps | findstr logcat')
		while True:
			log = result.readline().strip()
			if log and log.startswith("root"):
				os.system("adb -s " + dev + " shell kill " + log.split()[1])
			if log and not log.startswith("root"):
				continue
			if not log:
				break


# 获取手机已安装第三方应用包名
def getpacklist(Tdev):
	packlist2 = []
	packs = os.popen(os.getcwd() + '/tools/adb.exe -s ' + Tdev + ' shell pm list package -3')
	while True:
		pack = packs.readline().strip()
		if pack:
			packlist2.append(pack.split(':')[1])
		else:
			break
	return packlist2


# 获取手机驱动编号
def getdevices():
	devices = os.popen(os.getcwd() + '/tools/adb.exe devices')
	while True:
		dev = devices.readline().strip()
		if dev and dev.endswith('device'):
			devlist.append(dev.split()[0])
		elif dev and not dev.endswith('device'):
			continue
		elif not dev:
			break
	return devlist


# 获取当前时间
def getcurrenttime():
	nowtime = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
	return nowtime


# 定义apk列表
apklist = []
# 定义驱动列表
devlist = []
# 定义未安装apk包名列表
packlsit = []
# 定义已安装apk包名列表
packlist2 = []
print u'正在初始化......'
print u'please Wait for a moment......'

# 遍历文件夹下的apk
for apks in os.listdir('apklist/'):
	if apks.endswith(".apk"):
		allactivity, afera = getpackage(apks)
		packageall = allactivity.split('/')[0]
		packlsit.append(packageall)
		apklist.append(apks)

devlist = getdevices()
starttime = getcurrenttime()
for dev in devlist:
	os.system(os.getcwd() + '/tools/adb.exe -s ' + dev + ' shell svc power stayon true')
	for apk in apklist:
		activityname, name = getpackage(apk)
		packagename = activityname.split('/')[0]
		if 'com.tencent.android.qqdownloader' in activityname:
			activityname = 'com.tencent.android.qqdownloader/com.tencent.pangu.link.SplashActivityAlias0'
		elif 'me.ele' in activityname:
			activityname = 'me.ele/me.ele.Launcher'
		starttime1 = getcurrenttime()
		print starttime1 + ' start test : ' + packagename
		os.system(os.getcwd() + '/tools/adb.exe -s ' + dev + ' install -g ' + ' apklist/' + apk)
		time.sleep(10)
		os.system('echo ' + starttime1 + ' Test: ' + name + '>>' + starttime + '_' + dev + '.log')
		i = 0
		while i < 10:
			os.system(os.getcwd() + '/tools/adb.exe -s ' + dev + ' shell input keyevent 3')
			os.system(os.getcwd() + '/tools/adb.exe -s ' + dev + ' shell am force-stop ' + packagename)
			time.sleep(5)
			# 创建log文件夹
			path = os.getcwd() + '/log/' + starttime + '_' + dev + '/' + packagename
			if not os.path.exists(path):
				os.makedirs(path)
			# 抓取logcat
			logthrea = subprocess.Popen(
				os.getcwd() + '/tools/adb.exe -s ' + dev + ' shell  logcat -c && ' + os.getcwd() + '/tools/adb.exe -s ' + dev + ' shell  logcat >' + os.getcwd() + '/log/' + starttime + '_' + dev + '/' + packagename + '/' + str(
					i + 1) + '.log',
				stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE, close_fds=False)
			# 执行启动时延
			child = subprocess.Popen(
				os.getcwd() + '/tools/adb.exe -s ' + dev + ' shell am start -W -n ' + activityname + ' >> ' + starttime + '_' + dev + '.log',
				stdout=subprocess.PIPE, shell=True, stderr=subprocess.PIPE, close_fds=False)
			time.sleep(20)
			child.kill()
			os.system(os.getcwd() + '/tools/adb.exe -s ' + dev + ' shell input keyevent 3')
			os.system(os.getcwd() + '/tools/adb.exe -s ' + dev + ' shell am force-stop ' + packagename)
			# 停止抓logcat
			killlogcat(dev)
			logthrea.kill()
			i = i + 1
		packlist2 = getpacklist(dev)
		for pack in packlsit:
			if pack in packlist2:
				os.system(os.getcwd() + '/tools/adb.exe -s ' + dev + ' uninstall ' + pack)
print 'Completed'
