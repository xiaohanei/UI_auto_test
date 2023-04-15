from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException
from pubilc.pages.business_functions.Base import Base
from selenium.webdriver.common.action_chains import ActionChains
import os
import sys
# 获取根目录
BASE_DIR = "/Users/mac/Desktop/pythonProject/UI_auto_test"
# 将根目录添加到path中
sys.path.append(BASE_DIR)

class MouseAction(Base):
    def mouse_hover(self,by,loc):
        global abover
        attempt = 0
        while attempt < 3:
            try:
                try:
                    abover = self.driver.find_element(by,loc)
                    ActionChains(self.driver).move_to_element(abover).perform()
                except StaleElementReferenceException as msg:
                    attempt +=1
                    print(msg)
            except NoSuchElementException as msg:
                attempt +=1
                self.driver.refresh()
                print(msg)
        return abover