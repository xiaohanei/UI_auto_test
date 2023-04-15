from selenium import webdriver
from pubilc.tools.read_file import ReadFile
import re
from selenium.webdriver.chrome.options import Options
import os
import sys
# 获取根目录
BASE_DIR = "/Users/mac/Desktop/pythonProject/UI_auto_test"
# 将根目录添加到path中
sys.path.append(BASE_DIR)

def browser():
    # chrome_options = Options()
    # chrome_options.add_argument('--headless')
    # driver = webdriver.Chrome(chrome_options=chrome_options)
    driver = webdriver.Chrome()
    url = ReadFile().read_excel_not_include_header("UI_auto_test","config/test_environment_address.xlsx")[0][1]
    #通过正则表达式获取测试的url，去除来的时一个列表
    #url = re.findall('url=(.+?)\n',_url[0])[0]
    driver.get(url)
    return driver

if __name__ == '__main__':
    #browser()
    print(BASE_DIR)




