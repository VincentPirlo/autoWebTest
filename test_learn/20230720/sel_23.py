# _*_ coding: UTF-8 _*_
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.maximize_window()
# 等待时长10s，默认0.5s询问一次
WebDriverWait(driver, 10).until(lambda x: x.find_element(By.ID, 'kw').send_keys('selenium'))
time.sleep(1)


# 判断id为kw的元素是否消失
is_disappeared = WebDriverWait(driver, 10, 1).until_not(lambda x: x.find_element(By.ID, 'kw').is_displayed())
print(is_disappeared)

driver.quit()
