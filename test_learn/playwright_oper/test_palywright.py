from playwright.sync_api import sync_playwright
import time
# �Ϻ����� wx:283340479  
# blog:https://www.cnblogs.com/yoyoketang/

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, channel="chrome")          # ���� chromium �����
    page = browser.new_page()              # ��һ����ǩҳ
    page.goto("https://www.baidu.com")     # �򿪰ٶȵ�ַ
    print(page.title())                    # ��ӡ��ǰҳ��title
    time.sleep(5)
    browser.close()                        # �ر����������