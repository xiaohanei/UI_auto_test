from selenium.common import exceptions
from selenium.webdriver.common.by import By
from pubilc.pages.business_functions.Base import Base
from pubilc.pages.page_elements.login_page import LoginPage
from selenium.common.exceptions import NoSuchElementException
from pubilc.tools.read_file import ReadFile
import time
class Login(Base,LoginPage):
    test_datas = ReadFile().read_excel_include_header("UI_auto_test", "data/test_data.csv", '登录')
    #登录成功
    def login_Succcess(self):
        for test_data in self.test_datas:
            if test_data['remark'] == "login_success":
                attempt = 0
                while attempt < 3:
                    try:
                        self.driver.find_element(By.LINK_TEXT,self.loginSignin_button_loc).click()
                        self.driver.find_element(By.ID,self.username_loc).send_keys(int(test_data['username']))
                        self.driver.find_element(By.ID,self.password_loc).send_keys(test_data['password'])
                        self.driver.find_element(By.CLASS_NAME,self.login_button_loc).click()
                        break
                    except NoSuchElementException as msg:
                        attempt = attempt+1
                        self.driver.refresh()
                        print(msg)
    #登录时手机号输入错误
    def login_PhoneError(self):
        for test_data in self.test_datas:
            if test_data['remark'] == "phone_error":
                attempt = 0
                while attempt < 3:
                    try:
                        self.driver.find_element(By.LINK_TEXT,self.loginSignin_button_loc).click()
                        self.driver.find_element(By.ID,self.username_loc).send_keys(int(test_data['username']))
                        self.driver.find_element(By.ID,self.password_loc).send_keys(test_data['password'])
                        self.driver.find_element(By.CLASS_NAME,self.login_button_loc).click()
                        break
                    except NoSuchElementException as msg:
                        attempt = attempt+1
                        self.driver.refresh()
                        print(msg)

    # 登录时密码输入错误
    def login_PasswordError(self):
        for test_data in self.test_datas:
            if test_data['remark'] == "password_error":
                attempt = 0
                while attempt < 3:
                    try:
                        self.driver.find_element(By.LINK_TEXT, self.loginSignin_button_loc).click()
                        self.driver.find_element(By.ID, self.username_loc).send_keys(int(test_data['username']))
                        self.driver.find_element(By.ID, self.password_loc).send_keys(test_data['password'])
                        self.driver.find_element(By.CLASS_NAME, self.login_button_loc).click()
                        break
                    except NoSuchElementException as msg:
                        attempt = attempt+1
                        self.driver.refresh()
                        print(msg)
    #登录时不输入手机号
    def login_PhoneNull(self):
        for test_data in self.test_datas:
            if test_data['remark'] == "phone_null":
                attempt = 0
                while attempt < 3:
                    try:
                        self.driver.find_element(By.LINK_TEXT,self.loginSignin_button_loc).click()
                        self.driver.find_element(By.ID,self.username_loc).click()
                        self.driver.find_element(By.ID,self.password_loc).send_keys(test_data['password'])
                        self.driver.find_element(By.CLASS_NAME,self.login_button_loc).click()
                        break
                    except NoSuchElementException as msg:
                        attempt = attempt+1
                        self.driver.refresh()
                        print(msg)

    # 登录时不输入密码
    def login_PasswordNull(self):
        for test_data in self.test_datas:
            if test_data['remark'] == "password_null":
                attempt = 0
                while attempt < 3:
                    try:
                        self.driver.find_element(By.LINK_TEXT, self.loginSignin_button_loc).click()
                        self.driver.find_element(By.ID, self.username_loc).send_keys(int(test_data['username']))
                        self.driver.find_element(By.ID, self.password_loc).click()
                        self.driver.find_element(By.CLASS_NAME, self.login_button_loc).click()
                        break
                    except NoSuchElementException as msg:
                        attempt = attempt+1
                        self.driver.refresh()
                        print(msg)



