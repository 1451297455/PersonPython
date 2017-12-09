from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
browser = webdriver.Chrome('D:\chromedriver.exe', chrome_options=options)
browser.get("http://iot.ziyun-cloud.net/factoryweb/login.html")
username = browser.find_element_by_id('userName')
username.click()
username.send_keys("langel")
pwd = browser.find_element_by_id('pwd')
pwd.click()
pwd.send_keys("PASS1234")
code = browser.find_element_by_id('code')
checkcode = browser.find_elements_by_xpath('//div[@class="ub-f1 tx-c"]')
a = checkcode.__getitem__(0).text + checkcode.__getitem__(1).text + checkcode.__getitem__(
    2).text + checkcode.__getitem__(3).text
# for item in pages:
#     a = a + getattr(item)
print a
code.send_keys(a)
login = browser.find_element_by_id("checkLogin")
login.click()
time.sleep(2)
run = browser.find_element_by_id("li1")
run.click()
time.sleep(1)
run1 = browser.find_element_by_id('MachineParametersDiagnosis')
run1.click()
time.sleep(2)
totalpage = browser.find_element_by_xpath('//*[@id="page"]/span[@class="totalPages"]').text
nextpage = browser.find_element_by_xpath('//*[@id="nextPage"]')
curpage = browser.find_element_by_xpath('//*[@class="current"]').text
i = int(curpage)
while i < int(totalpage[1:2]):
    nextpage = browser.find_element_by_xpath('//*[@id="nextPage"]')
    nextpage.click()
    time.sleep(2)
    i = i + 1
    print i
# browser.close()
