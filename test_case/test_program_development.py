
from test_case.myunit import StartEnd
from pubilc.pages.business_functions.program_development import ProgramDevelopment
from pubilc.pages.page_elements.program_development_page import ProgramDevelopmentPage
from selenium.webdriver.common.by import By
import os
import sys
# 获取根目录
BASE_DIR = "/Users/mac/Desktop/pythonProject/UI_auto_test"
# 将根目录添加到path中
sys.path.append(BASE_DIR)

class TestProgramDevelopment(StartEnd,ProgramDevelopmentPage):
    def test_python_section_3_20(self):
        ProgramDevelopment(self.driver).python_section_3_20()
        self.assertIsNotNone(self.driver.find_element(By.XPATH,self.watch_python_section_3_20_loc))
    def test_python_section_3_21(self):
        ProgramDevelopment(self.driver).python_section_3_21()
        self.assertIsNotNone(self.driver.find_element(By.XPATH,self.watch_python_section_3_21_loc))
    def test_python_section_3_22(self):
        ProgramDevelopment(self.driver).python_section_3_22()
        self.assertIsNotNone(self.driver.find_element(By.XPATH,self.watch_python_section_3_22_loc))
    def test_python_section_3_23(self):
        ProgramDevelopment(self.driver).python_section_3_23()
        self.assertIsNotNone(self.driver.find_element(By.XPATH,self.watch_python_section_3_23_loc))
    def test_python_section_3_24(self):
        ProgramDevelopment(self.driver).python_section_3_24()
        self.assertIsNotNone(self.driver.find_element(By.XPATH,self.watch_python_section_3_24_loc))
    def test_python_section_3_25(self):
        ProgramDevelopment(self.driver).python_section_3_25()
        self.assertIsNotNone(self.driver.find_element(By.XPATH,self.watch_python_section_3_25_loc))

