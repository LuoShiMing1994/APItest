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
from HTMLTestRunner import HTMLTestRunner
import unittest,ddt

urlAPI = "../case/integralStore.xlsx"
dataAPI = performMethod.testMethod().getArguments(urlAPI)
@ddt.ddt
class runTest(unittest.TestCase):
    @ddt.data(*dataAPI)
    def test01(self,k):
        performMethod.testMethod().executeTest(k)
if __name__ == '__main__':
    # 初始化测试用例集合对象，构建测试套件
    testUnit = unittest.TestSuite()
    # 把测试用例加入到测试用例集合中去，将用例加入到检查套件中
    testUnit.addTest(unittest.TestLoader().loadTestsFromTestCase(runTest))
    # 定义测试报告，其中stream=测试报告生成路径，verbosity=测试报告详细等级，title=测试报告标题，description
    with open(r"../resultReport/report.html","wb+") as fp :
        HTMLTestRunner(stream=fp,verbosity=2,title="天马工场API测试报告",description="详细说明").run(testUnit)
    fp.close() #关闭d文件流