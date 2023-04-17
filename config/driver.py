from time import sleep

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
from pubilc.tools.get_jenkins_parameter import get_jenkis_parameter
def browser():
    # chrome_options = Options()
    # chrome_options.add_argument('--headless')
    # driver = webdriver.Chrome(chrome_options=chrome_options)
    driver = webdriver.Chrome()
    #url = ReadFile().read_excel_not_include_header("UI_auto_test","config/test_environment_address.xlsx")[0][1]
    for param in get_jenkis_parameter("http://localhost:8080/","UI_auto_test",'admin','11620ee242fbd91a1d247810ed518f479d'):
        if param['name'] =='environment':
            url = param['value']
            #print(url)
            driver.get(url)
    #通过正则表达式获取测试的url，去除来的时一个列表
    #url = re.findall('url=(.+?)\n',_url[0])[0]

    return driver

if __name__ == '__main__':
    browser()






