from test_case.myunit import StartEnd
from pubilc.pages.business_functions.user_center import UserCenter
from pubilc.pages.page_elements.user_center_page import UserCenterPage
from selenium.webdriver.common.by import By
import os
import sys
# 获取根目录
BASE_DIR = "/Users/mac/Desktop/pythonProject/UI_auto_test"
# 将根目录添加到path中
sys.path.append(BASE_DIR)
class TestUserCenter(StartEnd,UserCenterPage):
    def test_vip_center(self):
        UserCenter(self.driver).vip_center()
        self.assertIsNotNone(self.driver.find_element(By.XPATH,self.change_password_loc))

    def test_learning_record(self):
        UserCenter(self.driver).learning_record()
        self.assertIsNotNone(self.driver.find_element(By.CLASS_NAME,self.my_learning_speed_loc))
