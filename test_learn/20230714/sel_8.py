# _*_ coding: UTF-8 _*_
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.implicitly_wait(10)
driver.find_element(By.ID, 'kw').send_keys('软件测试')
time.sleep(3)
# 模拟enter键操作回车按钮
driver.find_element(By.ID, 'su').send_keys(Keys.ENTER)
time.sleep(3)
driver.quit()
