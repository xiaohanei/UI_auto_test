from test_case.myunit import StartEnd
from pubilc.pages.business_functions.login import Login
from pubilc.pages.page_elements.home_page import HomePage
from selenium.webdriver.common.by import By
from pubilc.pages.page_elements.login_page import LoginPage
from pubilc.tools.read_file import ReadFile
import os
import sys
# 获取根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 将根目录添加到path中
sys.path.append(BASE_DIR)
class TestLogin(StartEnd,HomePage,LoginPage):
    expected_results = ReadFile().read_excel_not_include_header("UI_auto_test", "data/expected_results.xlsx", '登录')
    #测试登录成功
    def test_login_succcess(self):
        Login(self.driver).login_Succcess()
        self.assertIsNotNone(self.driver.find_element(By.CLASS_NAME,self.user_name_loc))
    #测试手机号错误
    def test_login_PhoneError(self):
        Login(self.driver).login_PhoneError()
        for expected_result in self.expected_results:
            if expected_result[0] == "phone_error_msg":
                self.assertEqual(self.driver.find_element(By.CLASS_NAME,self.account_error_msg_loc).text,expected_result[1])
    #测试密码错误
    def test_login_PasswordError(self):
        Login(self.driver).login_PhoneError()
        for expected_result in self.expected_results:
            if expected_result[0] == "password_error_msg":
                self.assertEqual(self.driver.find_element(By.CLASS_NAME,self.account_error_msg_loc).text,expected_result[1])
    #测试手机号为空
    def test_login_PhoneNull(self):
        Login(self.driver).login_PhoneNull()
        for expected_result in self.expected_results:
            if expected_result[0] == "phone_null_msg":
                self.assertEqual(self.driver.find_element(By.ID,self.phone_null_msg_loc).text,expected_result[1])
    #测试密码为空
    def test_login_PasswordNull(self):
        Login(self.driver).login_PasswordNull()
        for expected_result in self.expected_results:
            if expected_result[0] == "password_null_msg":
                self.assertEqual(self.driver.find_element(By.ID,self.password_null_msg_loc).text,expected_result[1])



