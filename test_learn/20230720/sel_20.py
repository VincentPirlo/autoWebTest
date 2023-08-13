# _*_ coding: UTF-8 _*_
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.service import Service

# 配置文件地址
profile_directory = r'C:\Users\vincent\AppData\Roaming\Mozilla\Firefox\Profiles\ou5d8cq4.default'
# 加载配置
profile = webdriver.FirefoxProfile(profile_directory)
# 启动浏览器配置

options = Options()
# 指定firefox位置
options.binary_location = r"C:/Program Files/Mozilla Firefox/firefox.exe"
options.profile =
# 指定驱动geckodriver.exe位置
service = Service(r"C:/WebDriver/gecko/geckodriver.exe")
driver = webdriver.Firefox(options=options, service=service, profile=profile)
time.sleep(2)

driver.quit()
