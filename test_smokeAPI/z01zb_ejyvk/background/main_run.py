# -*- encoding: utf-8 -*-
"""
@File    : main_run.py
@Time    : 2019/12/31 11:01
@Author  : Liu Yuan
@Author_Email   : document.weite.get@gmail.com
@Software: PyCharm
@Description : 执行模块
"""
from test_smokeAPI.z01zb_ejyvk.background import liveTypeManager

class running:
    def run(self):
        id = liveTypeManager.liveBaseEdit().addChannel()
        print(id)

if __name__ == '__main__':
    strl = open("../../resources/str200.txt", "r", encoding="utf-8")
    print(type(strl.read()))