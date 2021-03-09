# coding = utf-8

from common.read_data import data
import os,re
# 设置系统字典，存放临时变量
dict_mongo={}

# 获取yaml数据

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

class yamlData():
    @staticmethod
    def getYamlData(file_path:str,key_name:str):
        data_file_path = os.path.join(BASE_PATH,'data',file_path)
        data_yaml = data.load_yaml(data_file_path).get(key_name)
        for key,value in data_yaml.items():
            if type(value) == str and ('${' in value):
                # data_yaml[key] = yamlData.parseString(value,caches)
                data_yaml.update({key:yamlData.parseString(value,dict_mongo)})
        return data_yaml

    @staticmethod
    def getYamlDataList(file_path:str,key_name:str):
        data_file_path = os.path.join(BASE_PATH,'data',file_path)
        data_yaml = data.load_yaml(data_file_path).get(key_name)
        for item in data_yaml:
            for key,value in item.items():
                if type(value) == str and ('${' in value):
                    item.update({key:yamlData.parseString(value,dict_mongo)})
        return data_yaml

    @staticmethod
    def parseString(content:str,caches:dict):
        m = re.finditer("\$\{(.+?)\}",content)
        for match in m:
            # 正则表达式匹配去除${}
            strs = re.sub('[\$\{\}]','',match.group())
            o = caches.get(strs)
            content = content.replace(match.group(),str(o))
        return content.strip()


# if __name__ == '__main__':
#     import time
#     dict_mongo.setdefault('time',str(time.time()))
#     a = yamlData.getYamlData('test_list.yaml','msg_list')
#     print(a)