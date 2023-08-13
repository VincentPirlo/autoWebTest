# _*_ coding: UTF-8 _*_
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("file:///D:/web_autoTest/test_learn/20230720/button.html")
driver.maximize_window()
time.sleep(2)

# 单选框radio
driver.find_element(By.ID, 'boy').click()
time.sleep(10)
driver.find_element(By.ID, 'girl').click()
time.sleep(2)

# 判断是否选中is_selected()
print(driver.find_element(By.ID, 'boy').is_selected())
print(driver.find_element(By.ID, 'girl').is_selected())

# 复选框checkbox
# 单个勾选
driver.find_element(By.ID, "c1").click()
time.sleep(2)

# 勾选全部
checkbox = driver.find_elements(By.XPATH, ".//*[@type='checkbox']")
for i in checkbox:
    i.click()
time.sleep(2)

driver.quit()
