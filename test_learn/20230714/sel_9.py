# _*_ coding: UTF-8 _*_
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.maximize_window()
driver.implicitly_wait(10)

# 鼠标悬停在搜索设置按钮上
mouse = driver.find_element(By.ID, 's-usersetting-top')
ActionChains(driver).move_to_element(mouse).perform()
time.sleep(2)
driver.quit()
