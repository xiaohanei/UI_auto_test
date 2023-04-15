import time

from selenium.common import exceptions
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException
from pubilc.pages.business_functions.Base import Base
from pubilc.pages.page_elements.program_development_page import ProgramDevelopmentPage
from selenium.webdriver.common.by import By
from pubilc.pages.page_elements.home_page import HomePage
from pubilc.pages.business_functions.login import Login
from pubilc.tools.mouse_action import MouseAction
from pubilc.tools.cookie_login import CookieLogin
import os
import sys
# 获取根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 将根目录添加到path中
sys.path.append(BASE_DIR)
class ProgramDevelopment(Base,ProgramDevelopmentPage,HomePage):
    def python_section_3_20(self):
        CookieLogin(self.driver).cookieLogin()
        attempt = 0
        while attempt < 3:
            try:
                try:
                    self.driver.find_element(By.LINK_TEXT,self.program_development_loc).click()
                    self.driver.find_element(By.LINK_TEXT,self.python_loc).click()
                    selenium_auto_cource_element = MouseAction(self.driver).mouse_hover(By.XPATH,self.selenium_auto_cource_loc)
                    selenium_auto_cource_element.click()
                    self.driver.switch_to.window(self.driver.window_handles[-1])
                    data_page2_element = MouseAction(self.driver).mouse_hover(By.LINK_TEXT,self.data_page2_loc)
                    data_page2_element.click()
                    python_section_3_20_title_element = MouseAction(self.driver).mouse_hover(By.XPATH,self.python_section_3_20_title_loc)
                    python_section_3_20_title_element.click()
                    self.driver.switch_to.window(self.driver.window_handles[-1])
                    break
                except StaleElementReferenceException as msg:
                    attempt = attempt+1
                    print(msg)
            except NoSuchElementException as msg:
                attempt = attempt + 1
                self.driver.refresh()
                print(msg)
    def python_section_3_21(self):
        CookieLogin(self.driver).cookieLogin()
        attempt = 0
        while attempt < 3:
            try:
                self.driver.find_element(By.LINK_TEXT,self.program_development_loc).click()
                self.driver.find_element(By.LINK_TEXT,self.python_loc).click()
                selenium_auto_cource_element = MouseAction(self.driver).mouse_hover(By.XPATH,self.selenium_auto_cource_loc)
                selenium_auto_cource_element.click()
                self.driver.switch_to.window(self.driver.window_handles[-1])
                data_page2_element = MouseAction(self.driver).mouse_hover(By.LINK_TEXT,self.data_page2_loc)
                data_page2_element.click()
                python_section_3_21_title_element = MouseAction(self.driver).mouse_hover(By.XPATH,self.python_section_3_21_title_loc)
                python_section_3_21_title_element.click()
                self.driver.switch_to.window(self.driver.window_handles[-1])
                break
            except exceptions as msg:
                attempt = attempt+1
                self.driver.refresh()
                print(msg)
    def python_section_3_22(self):
        CookieLogin(self.driver).cookieLogin()
        attempt = 0
        while attempt < 3:
            try:
                try:
                    self.driver.find_element(By.LINK_TEXT,self.program_development_loc).click()
                    self.driver.find_element(By.LINK_TEXT,self.python_loc).click()
                    selenium_auto_cource_element = MouseAction(self.driver).mouse_hover(By.XPATH,self.selenium_auto_cource_loc)
                    selenium_auto_cource_element.click()
                    self.driver.switch_to.window(self.driver.window_handles[-1])
                    data_page2_element = MouseAction(self.driver).mouse_hover(By.LINK_TEXT,self.data_page2_loc)
                    data_page2_element.click()
                    python_section_3_22_title_element = MouseAction(self.driver).mouse_hover(By.XPATH,self.python_section_3_22_title_loc)
                    python_section_3_22_title_element.click()
                    self.driver.switch_to.window(self.driver.window_handles[-1])
                    break
                except StaleElementReferenceException as msg:
                    attempt = attempt+1
                    print(msg)
            except NoSuchElementException as msg:
                attempt = attempt + 1
                self.driver.refresh()
                print(msg)

    def python_section_3_23(self):
        CookieLogin(self.driver).cookieLogin()
        attempt = 0
        while attempt < 3:
            try:
                try:
                    self.driver.find_element(By.LINK_TEXT, self.program_development_loc).click()
                    self.driver.find_element(By.LINK_TEXT, self.python_loc).click()
                    selenium_auto_cource_element = MouseAction(self.driver).mouse_hover(By.XPATH, self.selenium_auto_cource_loc)
                    selenium_auto_cource_element.click()
                    self.driver.switch_to.window(self.driver.window_handles[-1])
                    data_page2_element = MouseAction(self.driver).mouse_hover(By.LINK_TEXT, self.data_page2_loc)
                    data_page2_element.click()
                    python_section_3_23_title_element = MouseAction(self.driver).mouse_hover(By.XPATH,self.python_section_3_23_title_loc)
                    python_section_3_23_title_element.click()
                    self.driver.switch_to.window(self.driver.window_handles[-1])
                    break
                except StaleElementReferenceException as msg:
                    attempt = attempt+1
                    print(msg)
            except NoSuchElementException as msg:
                attempt = attempt + 1
                self.driver.refresh()
                print(msg)

    def python_section_3_24(self):
        CookieLogin(self.driver).cookieLogin()
        attempt = 0
        while attempt < 3:
            try:
                try:
                    self.driver.find_element(By.LINK_TEXT, self.program_development_loc).click()
                    self.driver.find_element(By.LINK_TEXT, self.python_loc).click()
                    selenium_auto_cource_element = MouseAction(self.driver).mouse_hover(By.XPATH, self.selenium_auto_cource_loc)
                    selenium_auto_cource_element.click()
                    self.driver.switch_to.window(self.driver.window_handles[-1])
                    data_page2_element = MouseAction(self.driver).mouse_hover(By.LINK_TEXT, self.data_page2_loc)
                    data_page2_element.click()
                    python_section_3_24_title_element = MouseAction(self.driver).mouse_hover(By.XPATH,self.python_section_3_24_title_loc)
                    python_section_3_24_title_element.click()
                    self.driver.switch_to.window(self.driver.window_handles[-1])
                    break
                except StaleElementReferenceException as msg:
                    attempt = attempt+1
                    print(msg)
            except NoSuchElementException as msg:
                attempt = attempt + 1
                self.driver.refresh()
                print(msg)
    def python_section_3_25(self):
        CookieLogin(self.driver).cookieLogin()
        attempt = 0
        while attempt < 3:
            try:
                try:
                    self.driver.find_element(By.LINK_TEXT, self.program_development_loc).click()
                    self.driver.find_element(By.LINK_TEXT, self.python_loc).click()
                    selenium_auto_cource_element = MouseAction(self.driver).mouse_hover(By.XPATH, self.selenium_auto_cource_loc)
                    selenium_auto_cource_element.click()
                    self.driver.switch_to.window(self.driver.window_handles[-1])
                    data_page2_element = MouseAction(self.driver).mouse_hover(By.LINK_TEXT, self.data_page2_loc)
                    data_page2_element.click()
                    python_section_3_25_title_element = MouseAction(self.driver).mouse_hover(By.XPATH,self.python_section_3_25_title_loc)
                    python_section_3_25_title_element.click()
                    self.driver.switch_to.window(self.driver.window_handles[-1])
                    break
                except StaleElementReferenceException as msg:
                    attempt = attempt+1
                    print(msg)
            except NoSuchElementException as msg:
                attempt = attempt + 1
                self.driver.refresh()
                print(msg)