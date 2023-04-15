
import time
from pubilc.tools.get_path import get_path
import os
import sys
# 获取根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 将根目录添加到path中
sys.path.append(BASE_DIR)

def now_time():
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    return now

def report_name():
    now = now_time()
    report_name = now + " report.html"
    return report_name