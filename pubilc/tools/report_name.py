
import time
from pubilc.tools.get_path import get_path
import os


def now_time():
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    return now

def report_name():
    now = now_time()
    report_name = now + " report.html"
    return report_name