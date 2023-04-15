from selenium import webdriver
from pubilc.tools.read_file import ReadFile
import re
from selenium.webdriver.chrome.options import Options

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
    browser()



