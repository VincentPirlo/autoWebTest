from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

# 窗口最大化
driver.maximize_window()
sleep(1)
# 设置窗口大小
driver.set_window_size(600, 600)
sleep(1)
# 窗口最小化
driver.minimize_window()
sleep(3)
driver.quit()
