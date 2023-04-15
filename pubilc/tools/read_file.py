

from pubilc.tools.get_path import get_path
import pandas
import os
import sys
# 获取根目录
BASE_DIR = "/Users/mac/Desktop/pythonProject/UI_auto_test"
# 将根目录添加到path中
sys.path.append(BASE_DIR)

class ReadFile():

    def read_txt(self,projectName,fileName):
        '''
        :param project_name: 项目名称
        :param fileName: 文件的名称，需要写上这个文件在整个项目上的多及路径，比如：test_enviroment_address.txt需要写成
                        "config/test_enviroment_address.txt"
        '''
        file_path = get_path(projectName,fileName)
        txt_file = open(file_path)
        url = txt_file.readlines()

        txt_file.close()
        print(url)
        return url

    def read_excel_include_header(self,projectName, fileName,sheetName="Sheet1"):
        '''
        该方法获取的表格中的数据带有表头。
        :param projectName: 项目名称
        :param fileName: 文件的名称，需要写上这个文件在整个项目上的多及路径，比如：test_enviroment_address.txt需要写成
                        "config/test_enviroment_address.txt"
        :param sheet_name: excel文件中每个sheet的名称
        :return:
        '''

        test_data = []
        #获取文件的路径
        file_path = get_path(projectName, fileName)
        #读取excel表格中的某个sheet
        file = pandas.read_excel(file_path,sheet_name=sheetName)
        #获取excel表格中的表头
        excel_item = file.columns
        #获取表格中最大行
        row = len(file.index)
        #i表示行数据，j表示列数据。都是从0开始的
        #将表格中的数据以列表嵌套字典的形式存储
        for i in range(row):
            j = 0
            data_dic = {}
            #将每一行的数据存储到一个字典中
            for item in excel_item:
                data_dic[item] = file.values[i][j]
                j = j+1
            test_data.append(data_dic)
        return test_data

    def read_excel_not_include_header(self,projectName, fileName,sheetName="Sheet1"):
        '''
                该方法获取的表格中的数据不带表头。
                :param projectName: 项目名称
                :param fileName: 文件的名称，需要写上这个文件在整个项目上的多及路径，比如：test_enviroment_address.txt需要写成
                                "config/test_enviroment_address.txt"
                :param sheet_name: excel文件中每个sheet的名称
                :return:
                '''
        file_path = get_path(projectName, fileName)
        file = pandas.read_excel(file_path, sheet_name=sheetName,header=None)
        test_data = file.values
        #print(test_data)
        return test_data












if __name__ == '__main__':
    #ReadFile().read_txt("UI_auto_test","config/test_environment_address.xlsx")
    test_datas = ReadFile().read_excel_include_header("UI_auto_test", "data/test_data.csv",'登录')
    expected_results = ReadFile().read_excel_not_include_header("UI_auto_test", "data/expected_results.xlsx",'登录')
    print(test_datas)
    print(expected_results)