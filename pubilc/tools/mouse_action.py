from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException
from pubilc.pages.business_functions.Base import Base
from selenium.webdriver.common.action_chains import ActionChains

class MouseAction(Base):
    def mouse_hover(self,by,loc):
        global abover
        try:
            abover = self.driver.find_element(by,loc)
            ActionChains(self.driver).move_to_element(abover).perform()
        except NoSuchElementException as msg:
            print(msg)

        return abover