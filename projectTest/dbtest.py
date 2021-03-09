# coding = utf-8

# from common.mysql_operate import db
from common.read_data import data
from common.Mongo import yamlData,dict_mongo
import os,time

base_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(base_path,'data','test_list.yaml')
def test1():
    data_yaml = data.load_yaml(data_file_path)
    sql = data_yaml.get('msg_list')
    print(sql)
    for item in sql:
        for key,value in item.items():
            print(key,value)
    # response = db.select_db(sql)
    # print(response)

def test2():
    dict_mongo.setdefault('time',str(time.time()))
    file_path = 'test_list.yaml'
    sql = yamlData.getYamlDataList(file_path,'msg_list')
    print(sql)
    # data_yaml = data.load_yaml(data_file_path)
    # sql = data_yaml.get('msg_list')
    # print(sql)
    # for item in sql:
    #     for key,value in item.items():
    #         if type(value) == str and ('${' in value):
    #             a = yamlData.parseString(value,dict_mongo)
    #             item.update({key:a})


    # print(sql)
if __name__ == '__main__':
    test2()