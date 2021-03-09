# coding = utf-8

import requests
from common.logger import logger
import json as complexjson

class RestClient():

    def __init__(self,api_host_test):
        self.api_host_test = api_host_test
        self.session = requests.session()

    def get(self,url,**kwargs):
        return self.request(url,"GET",**kwargs)

    def post(self,url,data=None,json=None,**kwargs):
        return self.request(url,data,json,**kwargs)

    def delete(self,url,**kwargs):
        return self.request(url,"DELETE",**kwargs)

    def put(self,url,data,**kwargs):
        return self.request(url,"PUT",data,**kwargs)

    def patch(self,url,data,**kwargs):
        return self.request(url,"PATCH",data,**kwargs)


    def request(self,url,method,data=None,json=None,**kwargs):
        url = self.api_host_test+url
        headers = dict(**kwargs).get("headers")
        params = dict(**kwargs).get("params")
        files = dict(**kwargs).get("params")
        cookies = dict(**kwargs).get("params")
        self.request_log(url,method,data,json,params,headers,files,cookies)
        if method =="GET":
            return self.session.get(url,**kwargs)
        if method == "POST":
            return self.session.post(url,data,json,**kwargs)
        if method =="PUT":
            if json:
                # PUT 和 PATCH 中没有提供直接使用json参数的方法，因此需要用data来传入
                data = complexjson.dumps(json)
            return self.session.put(url,data,**kwargs)
        if method == "DELETE":
            return self.session.delete(url,**kwargs)
        if method == "PATCH":
            return self.session.patch(url,data,**kwargs)


    def request_log(self,url, method, data=None, json=None, params=None, headers=None, files=None, cookies=None, **kwargs):
        logger.info("接口请求地址 ==>> {}".format(url))
        logger.info("接口请求方式 ==>> {}".format(method))
        # Python3中，json在做dumps操作时，会将中文转换成unicode编码，因此设置 ensure_ascii=False
        logger.info("接口请求头 ==>> {}".format(complexjson.dumps(headers, indent=4, ensure_ascii=False)))
        logger.info("接口请求 params 参数 ==>> {}".format(complexjson.dumps(params, indent=4, ensure_ascii=False)))
        logger.info("接口请求体 data 参数 ==>> {}".format(complexjson.dumps(data, indent=4, ensure_ascii=False)))
        logger.info("接口请求体 json 参数 ==>> {}".format(complexjson.dumps(json, indent=4, ensure_ascii=False)))
        logger.info("接口上传附件 files 参数 ==>> {}".format(files))
        logger.info("接口 cookies 参数 ==>> {}".format(complexjson.dumps(cookies, indent=4, ensure_ascii=False)))


