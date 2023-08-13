# _*_ coding: UTF-8 _*_
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.implicitly_wait(10)
driver.find_element(By.ID, 'kw').send_keys('软件测试')
time.sleep(3)
# submit()模拟enter键提交表单
driver.find_element(By.ID, 'kw').submit()
time.sleep(3)
driver.quit()
