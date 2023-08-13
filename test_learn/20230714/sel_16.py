# _*_ coding: UTF-8 _*_
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.service import Service

options = Options()
# 指定firefox位置
options.binary_location = r"C:/Program Files/Mozilla Firefox/firefox.exe"
# 指定驱动geckodriver.exe位置
service = Service(r"C:/WebDriver/gecko/geckodriver.exe")
driver = webdriver.Firefox(options=options, service=service)
# driver.maximize_window()
driver.set_window_size(40, 40)
driver.implicitly_wait(10)
time.sleep(2)

driver.find_element(By.ID, 'kw').send_keys('selenium')
# 元素聚焦
target = driver.find_element(By.ID, 'su')
driver.execute_script("arguments[0].scrollIntoView();", target)
target.click()
time.sleep(2)

driver.quit()
