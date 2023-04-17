import re

import jenkins
import requests
import json


def get_jenkis_parameter(jenkins_url, jenkins_job_name, jenkinss_username, API_token):
    '''
    username：登录jenkins的账号
    password：jenkins的API令牌（API Token）
    :param jenkins_job_name: 在jenkins上job的名称
    :return:
    '''
    jk = jenkins.Jenkins(url=jenkins_url, username=jenkinss_username, password=API_token)
    last_JobNumber = jk.get_job_info(jenkins_job_name)['lastBuild']['number']
    parameters = []
    jenkins_control_output = jk.get_build_console_output(jenkins_job_name, last_JobNumber+1)
    for each in jk.get_job_info(jenkins_job_name)['property']:
        if 'ParametersDefinitionProperty' in each['_class']:
            data = each['parameterDefinitions']
            for params in data:
                temp_dict = {}
                #print(params)
                temp_dict['name'] = params['defaultParameterValue']['name']
                temp_dict['value'] = re.findall(f'echo {params["defaultParameterValue"]["name"]}=(.+?)\n', jenkins_control_output)[0]
                temp_dict['description'] = params['description']
                parameters.append(temp_dict)
    print(parameters)

    return parameters
    # api_url = f"{jenkins_url}/job/{jenkins_job_name}/api/json?pretty=true"
    # reponse = requests.get(api_url,auth=(jenkinss_username,API_token))
    # data_json = json.loads(reponse.text)
    # data = data_json['actions']
    # parameters = []
    # for each in data:
    #     if each != {}:
    #         if 'ParametersDefinitionProperty' in each['_class']:
    #             data = each['parameterDefinitions']
    #             for params in data:
    #                 temp_dict = {}
    #                 temp_dict['name'] = params['name']
    #
    #                 temp_dict['value'] = params['defaultParameterValue']['value']
    #                 temp_dict['description'] = params['description']
    #                 parameters.append(temp_dict)
    # print(parameters)
    # return parameters




if __name__ == '__main__':
    get_jenkis_parameter("http://localhost:8080/", "UI_auto_test", 'admin', '11620ee242fbd91a1d247810ed518f479d')
