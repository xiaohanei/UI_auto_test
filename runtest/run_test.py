import unittest
from concurrent.futures.thread import ThreadPoolExecutor

from pubilc.tools.get_path import get_path
from pubilc.tools.report_name import report_name
from runtest.add_case import add_discover_case,run,get_case_list
from multiprocessing.pool import ThreadPool
from BeautifulReport import BeautifulReport
from pubilc.tools.report_name import now_time
from BSTestRunner import BSTestRunner
import os
import sys
# 获取根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 将根目录添加到path中
sys.path.append(BASE_DIR)

test_dir = get_path("UI_auto_test", "test_case")
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
report_dir = get_path("UI_auto_test", "reports")
report_file_name = report_name()
result = BeautifulReport(discover)
result.report(filename=report_file_name,description="login test",report_dir=report_dir)
# cases = add_discover_case()
# threadNum = 4
# pool = ThreadPool(threadNum)
# pool.map(run,get_case_list(cases))
# pool.close()
# pool.join()

