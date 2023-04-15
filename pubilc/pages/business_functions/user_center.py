from selenium.common import exceptions

from pubilc.pages.business_functions.Base import Base
from pubilc.pages.page_elements.home_page import HomePage
from pubilc.pages.page_elements.user_center_page import UserCenterPage
from pubilc.pages.business_functions.login import Login
from pubilc.tools.cookie_login import CookieLogin
from pubilc.tools.mouse_action import MouseAction
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException
from selenium.webdriver.common.by import By
import os
import sys
# 获取根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 将根目录添加到path中
sys.path.append(BASE_DIR)
class UserCenter(Base,HomePage,UserCenterPage):
    def vip_center(self):
        CookieLogin(self.driver).cookieLogin()
        attempt = 0
        while attempt < 3:
            MouseAction(self.driver).mouse_hover(By.CLASS_NAME,self.user_name_loc)
            try:
                try:
                    self.driver.find_element(By.LINK_TEXT,self.vip_center_loc).click()
                    break
                except StaleElementReferenceException as msg:
                    attempt = attempt+1
                    print(msg)
            except NoSuchElementException as msg:
                attempt = attempt + 1
                self.driver.refresh()
                print(msg)
    def learning_record(self):
        CookieLogin(self.driver).cookieLogin()
        attempt = 0
        while attempt < 3:
            MouseAction(self.driver).mouse_hover(By.CLASS_NAME, self.user_name_loc)
            try:
                try:
                    self.driver.find_element(By.LINK_TEXT,self.learning_record_loc).click()
                    break
                except StaleElementReferenceException as msg:
                    attempt = attempt+1
                    print(msg)
            except NoSuchElementException as msg:
                attempt = attempt + 1
                self.driver.refresh()
                print(msg)