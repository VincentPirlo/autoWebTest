# _*_ coding: UTF-8 _*_
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("file:///D:/web_autoTest/test_learn/20230720/table.html")
driver.maximize_window()
time.sleep(2)

t = driver.find_element(By.XPATH, ".//*[@id='myTable']/tbody/tr[2]/td[1]")
print(t.text)
time.sleep(1)

driver.quit()
