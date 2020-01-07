# -*- encoding: utf-8 -*-
"""
@File    : runCase.py
@Time    : 2020/1/7 19:10
@Author  : Liu Yuan
@Author_Email   : document.weite.get@gmail.com
@Software: PyCharm
@Description : 执行测试用例
"""
import unittest
from test_smokeAPI.z01zb_ejyvk.background import editLive,hostManager,liveManage,liveTypeManager
from HTMLTestRunner import HTMLTestRunner

class runTest(unittest.TestCase) :
    def setUp(self) -> None:
        pass
    def tearDown(self) -> None:
        pass
    def test_case_01(self): #主持人模块
        hostManager.hostM().run()
    def test_case_02(self): #直播频道管理
        liveTypeManager.liveBaseEdit().run()
    def test_case_03(self): #直播节目管理
        liveManage.live().run()
    def test_case_04(self): #直播节目设置管理
        editLive.setLive().run()


if __name__ == '__main__':
    # unittest.main()
    testUnit = unittest.TestSuite()
    testUnit.addTest(unittest.TestLoader().loadTestsFromTestCase(runTest))
    with open(r"../report/report.html","wb+") as fp :
        HTMLTestRunner(stream=fp,verbosity=2,title="天马工场API测试报告",description="详细说明").run(testUnit)
    fp.close() #关闭文件流