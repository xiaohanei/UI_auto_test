import os
import sys
# 获取根目录
BASE_DIR = "/Users/mac/Desktop/pythonProject/UI_auto_test"
# 将根目录添加到path中
sys.path.append(BASE_DIR)

class ProgramDevelopmentPage():
    #"类型"下面的python
    python_loc = "Python"
    #"Selenium自动化测试教程"课程
    selenium_auto_cource_loc = "//div[text()='Selenium自动化测试教程']"
    #Selenium自动化测试教程的第2业
    data_page2_loc = "2"
    #3-20,3-21,3-22,3-23,3-24,3-25课程
    python_section_3_20_title_loc = "//a[@title='3-20 文件处理']"
    python_section_3_21_title_loc = "//a[@title='3-21 读取txt文件']"
    python_section_3_22_title_loc = "//a[@title='3-22 CSV文件读写']"
    python_section_3_23_title_loc = "//a[@title='3-23 xml文件概述']"
    python_section_3_24_title_loc = "//a[@title='3-24 手工打造一个xml文件']"
    python_section_3_25_title_loc = "//a[@title='3-25 读取xml元素节点']"
    #观看课程3-20,3-21,3-22,3-23,3-24,3-25页面
    watch_python_section_3_20_loc = "//span[text()='3-20 文件处理']"
    watch_python_section_3_21_loc = "//span[text()='3-21 读取txt文件']"
    watch_python_section_3_22_loc = "//span[text()='3-22 CSV文件读写']"
    watch_python_section_3_23_loc = "//span[text()='3-23 xml文件概述']"
    watch_python_section_3_24_loc = "//span[text()='3-24 手工打造一个xml文件']"
    watch_python_section_3_25_loc = "//span[text()='3-25 读取xml元素节点']"
    #未登录状态下，观看课程，页面"快速登录"按钮
    quick_login_button_loc = "btn.btn-warning.size-l.radius"