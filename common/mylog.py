# -*- coding: utf-8 -*-
import logging
import os
import time


class MyLog(object):

    def __init__(self, logger=None):
        """
        phone_module 为手机型号
        指定保持日志的文件路径，日志级别，以及调用文件
        将日志存入指定的文件中
        :param logger:
        """
        # 日志文件夹，如果不存在则创建
        cur_path = os.path.dirname(os.path.realpath(__file__))
        log_path = os.path.join(os.path.dirname(cur_path), f'output\\logs')
        if not os.path.exists(log_path):
            os.mkdir(log_path)

        # log日期文件夹
        now_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        phone_log_path = os.path.join(os.path.dirname(cur_path), f'output\\logs\\{now_date}')
        if not os.path.exists(phone_log_path):
            os.mkdir(phone_log_path)

        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.INFO)

        # 创建一个handler，用于写入日志文件
        now_time = time.strftime('%Y%m%d-%H%M%S', time.localtime(time.time()))
        log_name = os.path.join(phone_log_path, f'{now_time}.log')
        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(levelname)s %(filename)s [line:%(lineno)d]; %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getLog(self):
        return self.logger
