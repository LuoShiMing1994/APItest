# -*- encoding: utf-8 -*-
"""
@File    : TenmaConfig.py
@Time    : 2019/10/31 18:13
@Author  : Liu Yuan
@Author_Email   : document.weite.get@gmail.com
@Software: PyCharm
@Description : 配置文件
"""
domain = "http://review.360tianma.com"
userData={                          #设置appium启动参数
    "platformName" : "Android",     #app所属系统
    "platformVersion" : "9.0.0",    #系统版本
    "automationName" : "appium",    #自动化平台名称
    "deviceName" : "7c2b89aa",      #测试的手机设备
    "autoAcceptAlterts" : "true",   #默认选择接受弹窗的条款
    "noRest" : "true",              #每次appium对app进行操作的时候，为了不保存修改的数据和app设置
                                    # 的内容而不影响下次使用，需要设置为true
    "appPackage" : "com.tenma.ventures.tianmagongchang",    #包名
    "appActivity" : "com.tenma.ventures.tianmagongchang.SplashActivity"     #类名
}
hostPath = "http://localhost:4723/wd/hub"