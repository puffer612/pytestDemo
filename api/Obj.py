# coding = utf-8

import os
from common.read_data import data
from core.rest_client import RestClient

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH,"config","setting.ini")
api_host_test = data.load_ini(data_file_path)["host_test"]["api_host_test"]
api_host_uat = data.load_ini(data_file_path)["host_uat"]["api_host_uat"]

class Obj(RestClient):

    def __init__(self,api_host_test):
        super(Obj,self).__init__(api_host_test)

    def getUrl(self,url,**kwargs):
        return self.get(url,**kwargs)

    def postUrl(self,url,**kwargs):
        return self.post(url,**kwargs)


obj = Obj(api_host_test)