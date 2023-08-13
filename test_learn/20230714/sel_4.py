# _*_ coding: UTF-8 _*_
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.maximize_window()
time.sleep(2)
# driver.get_screenshot_as_file("D:\\123\\baidu.jpg")
# driver.get_screenshot_as_png()
driver.save_screenshot('baidu.jpg')

