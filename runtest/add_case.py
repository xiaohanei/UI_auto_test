import unittest
from pubilc.tools.report_name import report_name
from pubilc.tools.get_path import get_path
from BSTestRunner import BSTestRunner
from BeautifulReport import BeautifulReport
import os
import sys
# 获取根目录
BASE_DIR = "/Users/mac/Desktop/pythonProject/UI_auto_test"
# 将根目录添加到path中
sys.path.append(BASE_DIR)


# test_dir = get_path("UI_auto_test", "test_case")
# # discover = unittest.defaultTestLoader.discover(test_dir,pattern='test_login.py')
# # discover = unittest.defaultTestLoader.discover(test_dir,pattern='test_computer_office.py')
# # discover = unittest.defaultTestLoader.discover(test_dir,pattern='test_user_center.py')
# discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
# report = report_name()
# with open(report,'wb') as f:
#     runner = BSTestRunner(stream=f,title="Test Report", description="login test")
#     runner.run(discover)
#     f.close()
def add_discover_case():
    test_dir = get_path("UI_auto_test", "test_case")
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
    return discover
def get_case_list(testunits):
    return [testunit for testunit in testunits]
def run(test_suits):
    report_dir = get_path("UI_auto_test", "reports")
    report_file_name = report_name()
    result = BeautifulReport(test_suits)
    result.report(filename=report_file_name,description="login test",report_dir=report_dir)

#
if __name__ == '__main__':
    cases = add_discover_case()
    print(cases)
    for case in cases:
        print(case)
        run(case)

