# _*_ coding: UTF-8 _*_
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
input_search = driver.find_element(By.ID, "kw")
input_search.send_keys("selenium")
driver.find_element(By.ID, "su").click()
time.sleep(3)

current_hand = driver.current_window_handle

# 打开新标签页
driver.find_element(By.XPATH, '//*[@id="help"]/a[4]').click()
print(driver.window_handles)

# 切换到新标签页
driver.switch_to.window(driver.window_handles[1])
print(driver.title)
# 关闭新标签页，回到之前的页面
time.sleep(2)
driver.close()
driver.switch_to.window(current_hand)
print(driver.title)
time.sleep(2)

driver.quit()

