from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
input_search = driver.find_element(By.ID, "kw")
input_search.send_keys("selenium")
driver.find_element(By.ID, "su").click()
time.sleep(3)


