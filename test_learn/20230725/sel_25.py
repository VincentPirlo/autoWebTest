# _*_ coding: UTF-8 _*_
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://www.baidu.com')
driver.maximize_window()
time.sleep(2)

print(driver.name)

driver.quit()
