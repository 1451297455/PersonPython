import os
import subprocess

p1 = subprocess.Popen('adb shell cd storage&&ls ', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
external = p1.stdout.read().split()[0].strip()
print external

files = os.listdir(os.getcwd())
for dirs in files:
	if dirs.startswith('Pic_3'):
		os.system('adb push Pic_3/. /storage/'+external+'/1/Pic_3')
os.system('adb shell am broadcast -a "sprd.intent.action.MEDIA_SCANNER_SCAN_DIR" --es scan_dir_path "/storage/'+external+'/1/Pic_3" -f 0x11000000')

