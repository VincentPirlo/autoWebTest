# _*_ coding: UTF-8 _*_
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.ID, 'kw').send_keys('selenium')
time.sleep(1)
driver.find_element(By.ID, 'kw').clear()
time.sleep(1)
driver.find_element(By.ID, 'kw').send_keys('selenium4')
time.sleep(1)
driver.find_element(By.ID, 'su').click()
time.sleep(1)
