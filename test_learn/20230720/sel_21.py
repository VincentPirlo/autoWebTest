# _*_ coding: UTF-8 _*_
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("file:///D:/web_autoTest/test_learn/20230720/inner_div.html")
driver.maximize_window()
time.sleep(2)

# 纵向底部
js1 = 'document.getElementById("yoyoketang").scrollTop=10000'
driver.execute_script(js1)
time.sleep(2)

# 纵向顶部
js2 = 'document.getElementById("yoyoketang").scrollTop=0'
driver.execute_script(js2)
time.sleep(2)

# 横向右侧
js3 = 'document.getElementById("yoyoketang").scrollLeft=10000'
driver.execute_script(js3)
time.sleep(2)

# 横向左侧
js4 = 'document.getElementById("yoyoketang").scrollLeft=0'
driver.execute_script(js4)
time.sleep(2)

# 获取的class返回的是list对象，取list的第一个
js5 = 'document.getElementsByClassName("scroll")[0].scrollTop=10000'
driver.execute_script(js5)
time.sleep(2)

# 控制横向滚动条位置
js6 = 'document.getElementsByClassName("scroll")[0].scrollLeft=10000'
driver.execute_script(js6)
time.sleep(2)


driver.quit()
