# download.py
# coding:utf-8

import urllib2
import os
import time
import shutil

lists = []


# 下载apk,例如QQ同步助手
def down(apkurl, path, dev):
	name = apkurl.split('/')[-1]
	if not os.path.exists(path + '\\' + name):
		apks = urllib2.urlopen(apkurl)
		data = apks.read()
		with open(path + '\\' + name, 'wb') as code:
			code.write(data)
	os.system("apk\case\AndroidAdb.exe -s " + dev + " install -g " + path + "\\" + name)


# apk 安装
def install(path, dev):
	if path == '11' or path == "28" or path == "Lowmem512" or path == "Lowmem1G" or path == "Lowmem2G" or path == "Lowmem3G":
		files = os.listdir("apk/" + path + '/')
		for apk in files:
			if apk.endswith('.apk'):
				# packageac = getpackage("apk/" + path + "/" + apk, dev)
				os.system('apk\case\AndroidAdb.exe -s ' + dev + ' install -g apk/' + path + '/' + apk)
				lists.append("")
	elif path == '0':
		lists.append("0")
	return lists


# 启动所有apk,home键挂后台
def launch(lists, dev):
	for item in lists:
		if item == "0":
			pass
		else:
			os.system("apk\case\AndroidAdb.exe -s " + dev + " shell am start -n " + item)
			time.sleep(5)
			os.system("apk\case\AndroidAdb.exe -s " + dev + " shell input keyevent 3")
			time.sleep(5)


def launchByUia(testname, dev):
	os.system(
		"apk\case\AndroidAdb.exe -s " + dev + " shell am instrument -w -r   -e debug false -e class com.spreadtrum.lowmemory.Background#" + testname + " com.spreadtrum.lowmemory.test/android.support.test.runner.AndroidJUnitRunner")


# 获取安装apk的包名和activity名
def getpackage(apk, dev):
	global package
	global activity
	infos = os.popen("apk\case\Aapt.exe  dump badging " + apk)
	while True:
		info = infos.readline()
		if info:
			if info.startswith("package:"):
				package = info.split('\'')[1]
				continue
			elif info.startswith('launchable-activity'):
				activity = info.split('\'')[1]
		else:
			break
	return package + '/' + activity


# 获取共享盘文件(单文件拷贝)
def getdata(sharePath, desFilename):
	fileList = os.listdir(sharePath)
	for filename in fileList:
		srcFilename = sharePath + '\\' + filename
		copyCommand = 'copy %s %s' % (srcFilename, desFilename)
		if not os.path.exists(desFilename):
			os.makedirs(desFilename)
		print ('copyCommand' + copyCommand)
		if os.system(copyCommand) == 0:
			print ('copy successed!')
		else:
			print ('copy failed!')
		break


# 文件夹拷贝
def getdirs(shar, des):
	try:
		if os.path.exists(des):
			os.system('rd /s /q ' + des)
		shutil.copytree(shar, des)
		return True
	except:
		return False

# os.system("apk\case\AndroidAdb.exe push  " + des + "  /storage/emulated/0/app")
