# _*_ coding: UTF-8 _*_
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
time.sleep(3)

# 关闭当前窗口
# driver.close()

# quit用于退出浏览器进程
driver.quit()
