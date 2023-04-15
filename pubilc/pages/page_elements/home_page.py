# import os
# import sys
# # 获取根目录
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# # 将根目录添加到path中
# sys.path.append(BASE_DIR)
class HomePage():
    # 登录成功后的首页元素
    #登录成功后用户名元素，通过class定位
    user_name_loc = 'text-overflow.mr-5'
    # 定位首页"电脑办公"按钮
    computer_office_loc = "电脑办公"
    #定位首页"程序开发"按钮
    program_development_loc = "程序开发"