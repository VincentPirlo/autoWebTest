# _*_ coding: UTF-8 _*_
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get('file:///D:/web_autoTest/test_learn/20230714/single_select.html')
driver.maximize_window()
driver.implicitly_wait(10)
time.sleep(2)

select_element = driver.find_element(By.NAME, 'selectomatic')
select_v = Select(select_element)
select_v.select_by_value('two')
time.sleep(2)

driver.quit()