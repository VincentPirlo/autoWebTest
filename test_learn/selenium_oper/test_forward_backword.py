from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

# 窗口最大化
driver.maximize_window()
sleep(1)
# 输入内容并搜索
input_search = driver.find_element(By.ID, "kw")
input_search.send_keys("selenium")
driver.find_element(By.ID, "su").click()
sleep(3)

driver.back()
sleep(1)
driver.forward()
sleep(3)
driver.refresh()
sleep(3)
# 输出当前url和窗口句柄
print(driver.current_url, driver.current_window_handle)
# 输出所有句柄
print(driver.window_handles)

driver.save_screenshot('baidu.png')
sleep(3)
driver.quit()
