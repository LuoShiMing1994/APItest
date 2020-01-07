# -*- encoding: utf-8 -*-
"""
@File    : requestPack.py
@Time    : 2019/12/31 14:14
@Author  : Liu Yuan
@Author_Email   : document.weite.get@gmail.com
@Software: PyCharm
@Description : 封装requests库
"""

import requests
from test_smokeAPI.z01zb_ejyvk.configs import url,header


class requestsMoudle:
    def __init__(self):
        pass
    def sendPost(self, formURL, formData):
        re = requests.post(url= url + formURL , data= formData , headers = header)
        return re
    def sendGet(self,formURL):
        re = requests.get(url= url + formURL ,headers = header)
        return re

# if __name__ == '__main__':
#     requestsMoudle().sendPost("/z01zb_ejyvk/Adminlive/updateLive",{"live_id" : 20 , "is_online" : 1 })