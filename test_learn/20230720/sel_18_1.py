# _*_ coding: UTF-8 _*_
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('file:///D:/web_autoTest/test_learn/20230720/alert_confirm_prompt.html')
time.sleep(3)

driver.find_element(By.ID, 'alert').click()
time.sleep(3)

t = driver.switch_to.alert

# 打印警告框文本内容
print(t.text)
# 点警告框文本内容
t.accept()
# t.dismiss()相当于点X按钮，取消
time.sleep(2)

driver.quit()