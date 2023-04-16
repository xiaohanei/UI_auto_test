import jenkins


def get_jenkis_parameter(jenkins_job_name):
    jk = jenkins.Jenkins(url="http://localhost:8080/",username="admin",password="11620ee242fbd91a1d247810ed518f479d")
    parameters = []
    for each in jk.get_job_info(jenkins_job_name)['property']:
        if 'ParametersDefinitionProperty' in each['_class']:
            data = each['parameterDefinitions']
            for params in data:
                temp_dict = dict()
                temp_dict['name'] = params['defaultParameterValue']['name']
                temp_dict['value'] = params['defaultParameterValue']['value']
                temp_dict['description'] = params['description']
                parameters.append(temp_dict)
                print(parameters)
                return parameters

if __name__ == '__main__':
    get_jenkis_parameter("UI_auto_test")
