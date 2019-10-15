# -*- encoding: utf-8 -*-
"""
@File    : run.py
@Time    : 2019/10/14 15:04
@Author  : Liu Yuan
@Author_Email   : document.weite.get@gmail.com
@Software: PyCharm
@Description : 控制台
"""
from tenmaLy.tools import readXlsx,assertions
import requests,unittest,ddt

urlAPI = "../platformsData/integralStore.xlsx"
dataAPI = readXlsx.get_xlsx(urlAPI).get_data_list()
@ddt.ddt
class runTest(unittest.TestCase):
    @ddt.data(*dataAPI)
    def test01(self,k):
        domain = "http://review.360tianma.com"
        shapeMethod = k["请求方法"]
        shapeAPI = k["接口地址"]
        shapeArgument = k["实参"]
        shapeResult = k["预期结果"]
        if shapeMethod == "GET" :
            actualRespones = requests.get(url=domain + shapeAPI)
            assertions.judgeResult().assertText(shapeResult,actualRespones.text)
        elif shapeMethod == "POST" :
            actualHeader = {"Content-Type":"application/x-www-form-urlencoded"}
            actualArgument = shapeArgument
            actualRespones = requests.post(url=domain + shapeAPI,data=actualArgument)
            assertions.judgeResult().assertText(shapeResult,actualRespones.text)
        else:
            print("您的请求方法不是POST or GET，请修改。")

if __name__ == '__main__':
    unittest.main()