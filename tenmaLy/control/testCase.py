# -*- encoding: utf-8 -*-
"""
@File    : testCase.py
@Time    : 2019/10/14 15:04
@Author  : Liu Yuan
@Author_Email   : document.weite.get@gmail.com
@Software: PyCharm
@Description : 控制台
"""
from tenmaLy.performModule import performMethod
import unittest,ddt

urlAPI = "../case/integralStore.xlsx"
dataAPI = performMethod.testMethod().getArguments(urlAPI)
@ddt.ddt
class runTest(unittest.TestCase):
    @ddt.data(*dataAPI)
    def test01(self,k):
        domain = "http://review.360tianma.com"
        performMethod.testMethod().executeTest(k,domain)

if __name__ == '__main__':
    unittest.main()
