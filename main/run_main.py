# -*- coding: utf-8 -*-
import os
import time
import pytest


if __name__ == '__main__':
    # 当前时间
    now_time = time.strftime('%Y%m%d-%H%M%S', time.localtime(time.time()))
    # allure 测试报告路径
    cur_path = os.path.dirname(os.path.realpath(__file__))
    report_path = os.path.join(os.path.dirname(cur_path), f'output\\report\\{now_time}')

    # -s: 打印信息
    # -m: 运行含标记的用例
    pytest.main(['-s', '-m', 'baidu_search or test_demo', '../test_cases/test_001_baiduSearch.py::TestBaiduSearch', '--alluredir', report_path])
    # 解析测试报告，运行：allure serve {report_path}
    os.system(f"allure serve {report_path}")

