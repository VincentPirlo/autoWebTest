# -*- coding: utf-8 -*-
from common.basePage import BasePage
from selenium.webdriver.common.by import By
from time import sleep


class BaiduIndex(BasePage):

    # 百度首页链接
    baidu_index_url = 'https://www.baidu.com'
    # 搜索框
    search_input = (By.ID, "kw")
    # "百度一下"按钮
    search_button = (By.ID, "su")

    # 查询操作
    def search_key(self, search_key):
        self.logger.info("[===搜索操作===]")
        # 等待用户名文本框元素出现
        self.wait_eleVisible(self.search_input, model='搜索框')
        # 输入内容
        self.input_text(self.search_input, "萝卜", model='搜索框')
        # 清除文本框内容
        self.clean_inputText(self.search_input, model='搜索框')
        # 输入用户名
        self.input_text(self.search_input, text=search_key, model='搜索框')
        # 等待搜索按钮出现
        self.wait_eleVisible(self.search_button, model='"百度一下"搜索按钮')
        # 点击搜索按钮
        self.click_element(self.search_button, model='"百度一下"搜索按钮')
        # 搜索后等待界面加载完成
        self.driver.implicitly_wait(10)
        sleep(3)
