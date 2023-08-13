# _*_ coding: UTF-8 _*_
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://www.baidu.com')
driver.maximize_window()
time.sleep(2)

driver.find_element(By.ID, 'kw').send_keys('selenium')
time.sleep(2)
# 获取百度输入框的联想词
bd = driver.find_elements(By.CLASS_NAME, 'bdsug-overflow')
for i in bd:
    print(i.get_attribute('data-key'))
time.sleep(2)

# 点击其中的一个
if len(bd) > 1:
    bd[1].click()
    print(driver.current_url)
else:
    print('未获取到匹配的词')
time.sleep(2)

driver.quit()
