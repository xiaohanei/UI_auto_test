

import os
import sys
# 获取根目录
BASE_DIR = "/Users/mac/Desktop/pythonProject/UI_auto_test"
# 将根目录添加到path中
sys.path.append(BASE_DIR)
class LoginPage():
    # 首页登录/注册按钮，通过link_text定位
    loginSignin_button_loc = '登录/注册'
    # 用户名手机号邮箱输入框，通过id定位
    username_loc = 'loginStr'
    # 密码输入框，通过id定位
    password_loc = 'pwd'
    #登录弹窗上的登录按钮,通过class定位
    login_button_loc = 'btn.radius.size-L.btn-danger'
    #登录弹窗上手机号/密码输入错误，点击登录后文字提示元素，通过class定位
    account_error_msg_loc = 'msgText.error'
    #登录弹窗上手机号为空，点击登录按钮后文字提示元素，通过id定位
    phone_null_msg_loc = 'loginStr-error'
    # 登录弹窗上密码为空，点击登录按钮后文字提示元素，通过id定位
    password_null_msg_loc = 'pwd-error'