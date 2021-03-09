# coding = utf-8

import json
from api.Obj import obj
import jmespath

class UserInfo():

    def __init__(self):
        pass
    def getCaptcha(self):
        url = 'sc/captcha/captcha'
        data = {
            'scene': 'uc_login'
        }
        param = {
            'params': json.dumps(data, ensure_ascii=False),
            'ctype': 'YOULU.WEB'
        }
        result = obj.getUrl(url,params=param)
        captcha =jmespath.search('data',result.json())
        return captcha

    def login(self):
        url = 'uc/login'
        data = {
            'userLoginname': '',
            'userLoginpwd': '123456',
            'userMobile': '18310325608',
            'userEmail': '',
            'verify': '',
            'captcha': self.getCaptcha(),
            'userFlag': 'S',
            'clueExtension':'',
            'behaviorExtension':'',
            'extensionType': ''
        }
        param = {
            'params': json.dumps(data,ensure_ascii=False),
            'ctype': 'YOULU.WEB'
        }
        result = obj.getUrl(url,params=param)
        # print(result.json())
        token = jmespath.search('data.token',result.json())
        return token
token = UserInfo().login()

# if __name__ == '__main__':
#     print(token)

