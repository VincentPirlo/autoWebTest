# _*_ coding: UTF-8 _*_
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
time.sleep(3)

# 将浏览器窗口最大化
driver.maximize_window()
time.sleep(3)

# 将浏览器窗口设置为960*540
driver.set_window_size(960, 540)
time.sleep(3)

# 将浏览器窗口最小化
driver.minimize_window()
