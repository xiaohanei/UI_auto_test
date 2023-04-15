from selenium.webdriver.common.by import By
from pubilc.pages.business_functions.Base import Base
from pubilc.pages.page_elements.computer_office_page import ComputerOfficePage
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException
import os
import sys
# 获取根目录
BASE_DIR = "/Users/mac/Desktop/pythonProject/UI_auto_test"
# 将根目录添加到path中
sys.path.append(BASE_DIR)
class GetCourses(Base,ComputerOfficePage):
    def get_courses(self):
        global courses
        attempt = 0
        while attempt <3:
            try:
                try:
                    elements = self.driver.find_elements(By.XPATH, self.courses_loc)
                    courses = []
                    for i in range(len(elements)):
                        courses.append(elements[i].text)
                    break

                except StaleElementReferenceException as msg:
                    attempt +=1
                    print(msg)
            except NoSuchElementException as msg:
                attempt +=1
                self.driver.refresh()
                print(msg)
            finally:
                return courses
