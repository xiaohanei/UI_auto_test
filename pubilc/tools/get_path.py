import os

def get_path(project_name,fileName):
    '''

    :param project_name: 项目名称
    :param fileName: 文件的名称，需要写上这个文件在整个项目上的多及路径，比如：test_enviroment_address.txt需要写成
                        "config/test_enviroment_address.txt"
    :return:
    '''
    #获取当前文件的路径
    cur_path = os.path.abspath(__file__)
    #获取整个项目的跟路径
    project_path = cur_path[:cur_path.find(project_name)]+project_name
    #获取制定文件的路径
    file_path = os.path.join(project_path,fileName)
    print(file_path)
    return file_path


if __name__ == '__main__':
    get_path("UI_auto_test","config")
