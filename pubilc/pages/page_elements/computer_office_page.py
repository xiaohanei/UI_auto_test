
import os
import sys
# 获取根目录
BASE_DIR = "/Users/mac/Desktop/pythonProject/UI_auto_test"
# 将根目录添加到path中
sys.path.append(BASE_DIR)
class ComputerOfficePage():

    #电脑办公页面"类型"下面各种选项的元素定位，通过超链接文本定位
    type_unlimited_loc = "//div[@id='soft']/a"     #因为有两个不限，从父级开始定位，使用xpath路径,定位类型下面的不限
    computer_primary_loc = "电脑入门"
    five_stroke_loc = "五笔输入法86版"
    word_loc = "Word"
    ppt_loc = "PPT"
    excel_base_loc = "Excel 基础"
    excel_progress_loc = "Excel 进阶"
    wps_loc = "WPS"
    #电脑办公页面"等级"下面各种选项的元素定位
    rank_unlimited_loc = "//div[@id='rank']/a"  #因为有两个不限，从父级开始定位，使用xpath路径，定位等级下面的不限
    primary_loc = "入门"
    progress_loc = "进阶"
    senior_loc = "高级"
    #电脑办公页面"排序"下面各种选项的元素定位
    default_sort_loc = "默认排序"
    last_loc = "最新"
    most_followed_loc = "最多关注"
    visits_loc = "访问量"
    #各个类型下面所有课程,通过find_elements获取
    courses_loc = "//div[@class='courses']//div[@class='name text-l']"
