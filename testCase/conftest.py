# coding = utf-8

import pytest
import allure
from api.Obj import obj
from common.read_data import data
from common.mysql_operate import db
from common.logger import logger
from operation.userToken import token





@allure.step("前置条件---> 清理数据")
def step_frist():
    logger.info("*******")
    logger.info("清理数据")

@allure.step("后置条件---> 清理数据")
def step_last():
    logger.info("后置条件开始，清除数据")

@pytest.fixture(scope='session',autouse=True)
def token_fixture():
    logger.info('获取当前用户的token信息为{}'.format(token))
    yield token


'''
清除测试数据数据
'''
# @pytest.fixture(scope='session')
# def assert_data():
#     sql = data.load_yaml('')
