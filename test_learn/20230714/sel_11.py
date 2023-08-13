# _*_ coding: UTF-8 _*_
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://mail.163.com/')
driver.maximize_window()
driver.implicitly_wait(10)
time.sleep(2)

# 切换iframe
iframe = driver.find_element(By.XPATH, '//iframe[starts-with(@id, "x-URS-iframe")]')
driver.switch_to.frame(iframe)
driver.find_element(By.NAME, 'email').send_keys("123")
time.sleep(2)
driver.find_element(By.NAME, 'password').send_keys("345")
time.sleep(2)

# 释放iframe，重新回到主页面上
driver.switch_to.default_content()
driver.quit()
