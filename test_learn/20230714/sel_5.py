# _*_ coding: UTF-8 _*_
import random
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.implicitly_wait(10)
driver.find_element(By.ID, 'kw').send_keys(u"测试部落")
driver.find_element(By.ID, 'kw').submit()
s = driver.find_elements(By.CSS_SELECTOR, "h3.t>a")

t = random.randint(0, 9)
a = s[t].get_attribute('href')
print(a)
driver.get(a)