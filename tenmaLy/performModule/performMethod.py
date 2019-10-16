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
import requests

class testMethod:
    def getArguments(self,expectUrl):   #获取需要遍历的数据
        __urlAPI = expectUrl
        __dataAPI = readXlsx.get_xlsx(__urlAPI).get_data_list()
        return __dataAPI
    def executeTest(self,k):    #这里传入的参数必须是一个字典
        __actulDomain = k["域名"]
        __expectMethod = k["请求方法"]
        __expectAPI = k["接口地址"]
        __expectHeader = k["头部"]
        __expectArgument = k["实参"]
        __expectResult = k["预期结果"]
        if __expectMethod == "GET" :
            print("正在比对结果，请稍等...")
            actualRespones = requests.get(url=__actulDomain + __expectAPI)
            assertions.judgeResult().assertText(__expectResult, actualRespones.text)
        elif __expectMethod == "POST" :
            print("正在比对结果，请稍等...")
            actualArgument = __expectArgument
            actualRespones = requests.post(url=__actulDomain + __expectAPI,data=actualArgument)
            assertions.judgeResult().assertText(__expectResult, actualRespones.text)
        else:
            print("您的请求方法不是POST or GET，请修改。")