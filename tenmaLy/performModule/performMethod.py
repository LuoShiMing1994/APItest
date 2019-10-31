# -*- encoding: utf-8 -*-
"""
@File    : performMethod.py
@Time    : 2019/10/15 18:50
@Author  : Liu Yuan
@Author_Email   : document.weite.get@gmail.com
@Software: PyCharm
@Description : 用于执行用例的模块
"""

from tenmaLy.tools import assertions
from tenmaLy.tools import readXlsx
import requests,json

class testMethod:
    def getArguments(self,expectUrl):   #expectUrl：case的存放路径
        __urlAPI = expectUrl
        __dataAPI = readXlsx.get_xlsx(__urlAPI).get_data_list()
        return __dataAPI
    def executeTest(self,k):    #k是一个字典
        __actulDomain,__expectMethod,__expectAPI,__expectArgument,__expectResult,__expectHeaders = \
            k["domain"],k["method"],k["path"],k["data"],k["expect_status_code"],k["headers"]
        if __expectMethod == "GET" :
            actualRespones = requests.get(url=__actulDomain + __expectAPI,headers=json.loads(__expectHeaders))
            print(__expectArgument)
            assertions.judgeResult().assertText(__expectResult, actualRespones.status_code)
        elif __expectMethod == "POST" :
            actualRespones = requests.post(url=__actulDomain + __expectAPI,data=json.loads(__expectArgument),
                                           headers=json.loads(__expectHeaders))
            assertions.judgeResult().assertText(__expectResult, actualRespones.status_code)
        else:
            print("请求方法错误")
            print("您的请求方法不是POST or GET，请修改。")