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
    def getArguments(self,expectUrl):   #获取需要遍历的数据
        __urlAPI = expectUrl
        __dataAPI = readXlsx.get_xlsx(__urlAPI).get_data_list()
        return __dataAPI
    def executeTest(self,k):    #这里传入的k是一个字典
        __actulDomain,__expectMethod,__expectAPI,__expectArgument,__expectResult,__expectHeaders = \
            k["domain"],k["method"],k["path"],k["data"],k["expect_status_code"],k["headers"]
        if __expectMethod == "GET" :
            actualRespones = requests.get(url=__actulDomain + __expectAPI)
            print(__expectArgument)
            assertions.judgeResult().assertText(__expectResult, actualRespones.status_code)
        elif __expectMethod == "POST" :
            actualRespones = requests.post(url=__actulDomain + __expectAPI,data=__expectArgument,headers=json.loads(__expectHeaders))
            print("预计状态码：%d"%__expectResult)
            # print(actualRespones.text)
            assertions.judgeResult().assertText(__expectResult, actualRespones.status_code)
        else:
            print("请求方法错误")
            print("您的请求方法不是POST or GET，请修改。")