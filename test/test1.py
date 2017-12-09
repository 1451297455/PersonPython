# coding:utf-8
from appium import webdriver

desired_caps = {'platformName': 'Android', 'platformVersion': '23', 'deviceName': 'DA061XXXXXX68SO00073',
                'appPackage': 'com.android.calculator2', 'appActivity': '.Calculator'}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

driver.find_element_by_name("1").click()

driver.find_element_by_name("5").click()

driver.find_element_by_name("9").click()

driver.find_element_by_name("删除").click()

driver.find_element_by_name("9").click()

driver.find_element_by_name("5").click()

driver.find_element_by_name("+").click()

driver.find_element_by_name("6").click()

driver.find_element_by_name("=").click()

driver.quit()
