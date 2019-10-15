# -*- encoding: utf-8 -*-
"""
@File    : assertions.py
@Time    : 2019/8/28 21:27
@Author  : Liu Yuan
@Author_Email   : selenium_requests@qq.com
@Software: PyCharm
@Description : 断言工具
"""
class judgeResult:
    def assertText(self,expectedResults,actualResults):
        try:
            assert expectedResults in actualResults
            print("无效用例")
        except :
            print("有效用例")
            return print("报错参数：" + actualResults)
