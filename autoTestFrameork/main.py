import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

chrome = webdriver.Remote( command_executor='http://192.168.47.140:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
firefox = webdriver.Remote( command_executor='http://192.168.47.140:4444/wd/hub', desired_capabilities=DesiredCapabilities.FIREFOX)
start = time.time()
for i in range(100):
    chrome.get('https://www.qq.com')
    print(chrome.title,i)
print(time.time() - start)