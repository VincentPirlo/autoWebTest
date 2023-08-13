# _*_ coding: UTF-8 _*_
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
# driver.maximize_window()
driver.set_window_size(800, 800)
driver.implicitly_wait(10)
time.sleep(2)

driver.find_element(By.ID, 'kw').send_keys('selenium')
driver.find_element(By.ID, 'su').click()
time.sleep(2)

# 向下滚动
js = "var q=document.documentElement.scrollTop=10000"
driver.execute_script(js)
time.sleep(2)

# 向上滚动
js1 = "var q=document.documentElement.scrollTop=0"
driver.execute_script(js1)
time.sleep(2)

# 左右滚动
js2 = "window.scrollTo(100,100);"
driver.execute_script(js2)
time.sleep(2)

driver.quit()