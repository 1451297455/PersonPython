# coding:utf-8
from appium import webdriver
from selenium.webdriver.common.by import By

descp = {'platformName': 'Android', 'platformVersion': '23', 'deviceName': 'DA061XXXXXX68SO00073',
         'appPackage': 'com.qiyi.video', 'appActivity': '.WelcomeActivity'}
device = webdriver.Remote('http://127.0.0.1:4723/wd/hub', descp)
elem = device.find_element_by_name('电视剧')
elem.click()
device.swipe(360, 1000, 360, 400)
elem1 = device.find_element_by_android_uiautomator('a')
# x = device.
# print x
# y = device.get_window_rect()
# print y
device.tap([(100, 300)], 1)
device.close()
