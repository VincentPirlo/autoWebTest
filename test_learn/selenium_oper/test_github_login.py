import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://github.com/login")
driver.implicitly_wait(10)
driver.maximize_window()

driver.find_element(By.ID, "login_field").send_keys("123@163.com")
driver.find_element(By.ID, "password").send_keys("123")

time.sleep(5)
driver.quit()
