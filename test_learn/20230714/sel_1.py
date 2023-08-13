# _*_ coding: UTF-8 _*_
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
time.sleep(3)

driver.get('https://zhuanlan.zhihu.com/')
time.sleep(3)
# 返回上一页
driver.back()
time.sleep(3)
# 切换到下一页
driver.forward()
