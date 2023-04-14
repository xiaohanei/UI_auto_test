

class UserCenterPage():
    #"会员中心"按钮，通过link_text的方式定位
    vip_center_loc = "会员中心"
    #"学习记录"按钮，通过link_text的方式定位
    learning_record_loc = "学习记录"
    #进入会员中心页面，"修改密码"按钮，通过xpath来定位
    change_password_loc = "//div[text()='修改密码']"
    #进入学习进度页面，"我的学习进度"文案，通过class来定位
    my_learning_speed_loc = "navLinks.pb-20.f-14"