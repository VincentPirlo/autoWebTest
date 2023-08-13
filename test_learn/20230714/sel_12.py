# _*_ coding: UTF-8 _*_
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.maximize_window()
driver.implicitly_wait(10)
time.sleep(2)

mouse = driver.find_element(By.ID, 's-usersetting-top')
ActionChains(driver).move_to_element(mouse).perform()
time.sleep(2)

ActionChains(driver).click(driver.find_element(By.XPATH, '//*[@id="s-user-setting-menu"]/div/a[2]/span')).perform()
# driver.find_element(By.XPATH, '//*[@id="u"]/div/a[2]/span').click()
time.sleep(2)

driver.find_element(By.CLASS_NAME, 'c-select-selection').click()
time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="adv-setting-gpc"]/div/div[2]/div[2]/p[3]').click()
time.sleep(2)

driver.quit()
