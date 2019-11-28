# -*- encoding: utf-8 -*-
"""
@File    : OPAction.py
@Time    : 2019/11/18 19:21
@Author  : Liu Yuan
@Author_Email   : document.weite.get@gmail.com
@Software: PyCharm
@Description : 动作控件
"""

import uiautomator2 as u2
import os,time

        
class userAction:
    def __init__(self,packName): #连接手机
        connectCmd = os.popen("adb devices")
        intC, resultsLines = connectCmd.read(), []
        for line in intC.splitlines(): resultsLines.append(line)
        __devicesNo = resultsLines[1].split()[0]
        self.__mobileD = u2.connect(__devicesNo)  # 如果设备和PC电脑在同一局域网的话，还可以是你的设备IP地址。
        self.__mobileD.app_clear(packName)  #清除app数据
        self.__mobileD.app_start(packName)  # 启动app
        # self.__mobileD.app_stop(packName)
        # self.__mobileD.implicitly_wait(10)
        time.sleep(20)
        print("测试环境已清理完毕，请稍后...")
    def getClassName(self,local):
        self.__mobileD(className=local).click()
        print("已点击")
    def getResourceId(self,local):
        self.__mobileD(resourceId=local).click()
    def getText(self,local):
        self.__mobileD(text=local).click()
    def getDescription(self,local):
        self.__mobileD(description=local).click()

if __name__ == '__main__':
    packName = "com.tenma.ventures.tianmagongchang"
    uA = userAction(packName)
    count = 0
    shiting = "视听"
    xinshidai = "新时代"
    for i in range(100) :
        uA.getText(shiting)
        uA.getText(xinshidai)
        count += 1
        print(count)
