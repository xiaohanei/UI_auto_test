import unittest
from config.driver import browser
import os
import sys
# 获取根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 将根目录添加到path中
sys.path.append(BASE_DIR)

class StartEnd(unittest.TestCase):
    def setUp(self):
        self.driver = browser()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()
