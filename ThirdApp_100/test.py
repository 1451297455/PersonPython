import os


def getpacklist():
	packs = os.popen('adb  shell pm list package -3')
	while True:
		pack = packs.readline().strip()
		if pack:
			print pack.split(':')[1]
			packlist2.append(pack.split(':')[1])
		else:
			break
	return packlist2


packlist2 = []
# result = os.popen('adb shell ps | findstr logcat')
# while True:
# 	log = result.readline().strip()
# 	if log and log.startswith("root"):
# 		os.system("adb shell kill "+log.split()[1])
# 	if log and not log.startswith("root"):
# 		continue
# 	if not log:
# 		break
starttime = 'qwqweqw'
dev = 'SC98321E10079050673'
packagename = 'asss'

# i = 1
# path = os.getcwd() + '/log/' + starttime + '_' + dev + '/' + packagename
# if not os.path.exists(path):
# 	os.makedirs(path)
# os.system(
# 	'adb -s ' + dev + ' shell  logcat -c && adb -s ' + dev + ' shell  logcat >log/' + starttime + '_' + dev + '/' + packagename + '/' + str(
# 		i) + '.log')
#
#
# # for pac in getpacklist():
# # 	print pac

adb = os.getcwd() + '/tool/adb.exe'


def killlogcat(dev):
	version = os.popen('adb  -s ' + dev + ' shell getprop | findstr version.release')
	pslogcat = version.readline().strip()
	if '8' in pslogcat:
		result = os.popen('adb -s ' + dev + ' shell ps -All | findstr logcat')
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


killlogcat(dev)
