from selenium import webdriver
from time import sleep
from pubilc.pages.business_functions.Base import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.driver import browser
from selenium.webdriver.common.by import By

from pubilc.pages.page_elements.home_page import HomePage
import os
import sys
# 获取根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 将根目录添加到path中
sys.path.append(BASE_DIR)


class CookieLogin(Base,HomePage):
    def cookieLogin(self):
        #driver = browser()
        # driver.maximize_window()
        self.driver.add_cookie({"name":"newsMember","value":"4Ih6VNjKGSNvY2cDyp4NI6yQYZCG9gLrxx1PeYPF8OTW1NHWAp0EKY7eVpJTN3uPWiBV5PRVl7AhKH6vShNb2Q1cCN/FQsiQPXy6iGqVF6w="})
        self.driver.refresh()
        WebDriverWait(self.driver,20,1).until(EC.presence_of_element_located((By.CLASS_NAME,self.user_name_loc)))
        #sleep(10)


if __name__ == '__main__':
    driver = browser()
    CookieLogin(driver).cookieLogin()


