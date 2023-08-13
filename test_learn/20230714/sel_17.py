# _*_ coding: UTF-8 _*_
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
# driver.maximize_window()
driver.set_window_size(800, 800)
driver.implicitly_wait(10)
print(driver.name)
time.sleep(2)

driver.find_element(By.ID, 'kw').send_keys('selenium')
driver.find_element(By.ID, 'su').click()
time.sleep(2)

# 滚动到底部
js1 = "window.scrollTo(0, document.body.scrollHeight)"
driver.execute_script(js1)
time.sleep(2)

# 滚动到顶部
js2 = "window.scrollTo(0, 0)"
driver.execute_script(js2)
time.sleep(2)

driver.quit()
