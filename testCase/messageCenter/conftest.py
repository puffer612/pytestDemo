# coding=utf-8

from common.Mongo import dict_mongo,yamlData
import pytest
import time,json
from api.Obj import obj

@pytest.fixture(scope='function')
def test_MsgList_data(token_fixture):
    dict_mongo['time'] = str(time.time())
    file_path = 'test_list.yaml'
    key_name = 'msg_list'
    yaml_data = yamlData.getYamlDataList(file_path,key_name)
    token = token_fixture
    list = []
    for item in yaml_data:
        params = {
            'params': json.dumps(item,ensure_ascii=False),
            'ctype': 'YOULU.WEB',
            'TOKEN': token
        }

        response = obj.get('mc/my/msg/list',params=params)
        list.append(response)
    yield list

@pytest.fixture(scope='function')
def test_MsgList_data1(token_fixture):
    dict_mongo['time'] = str(time.time())
    file_path = 'test_list1.yaml'
    key_name = 'msg_list'
    yaml_data = yamlData.getYamlData(file_path,key_name)
    token = token_fixture
    params = {
        'params': json.dumps(yaml_data,ensure_ascii=False),
        'ctype': 'YOULU.WEB',
        'TOKEN': token
    }

    response = obj.get('mc/my/msg/list',params=params)
    yield response