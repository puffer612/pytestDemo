# coding = utf-8

import pytest
import allure
from common.logger import logger
import jmespath
# import coverage
# cov = coverage.coverage()
# cov.start()

class TestMsgList():

    @allure.story('获取消息列表---with token')
    @allure.description('获取该用户的消息列表信息')
    def test_msgList(self,test_MsgList_data1):
        logger.info('开始测试')
        response = test_MsgList_data1
        if response.status_code == 200 :
            res = response.json()
            datas = jmespath.search('data.count',res)
            assert datas == 9
            logger.info('test end')

# cov.stop()
# cov.save()

if __name__ == '__main__':
    pytest.main(['--html=../../reports/report.html', "test_msgList.py"])

