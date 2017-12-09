# coding:utf-8
import os

#获取设备型号
os.system('adb shell getprop ro.product.model >config.ini')
#获取系统android版本号
os.system('adb shell getprop ro.build.version.release >> config.ini')
#获取cpu信息
os.system('adb shell cat /proc/cpuinfo >> config.ini')
#获取屏幕分辨率
os.system('adb shell wm size >> config.ini')
#获取内存信息
os.system('adb shell cat /proc/meminfo >>config.ini')