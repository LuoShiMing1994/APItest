# -*- encoding: utf-8 -*-
"""
@File    : hostManager.py
@Time    : 2019/12/23 11:55
@Author  : Liu Yuan
@Author_Email   : document.weite.get@gmail.com
@Software: PyCharm
@Description : 主持人管理
"""

import requests,random
from test_smokeAPI.moudle_case.z01zb_ejyvk import configs as con

class hostM():
    def __init__(self):
        self.sess = requests.session()  # 获取一个session对象
        self.__url, self.__header, self.__randNum= con.url, con.header, con.randomN

    def addHost(self):  #新增主持人
        self.hostNum = random.randint(20,19900)  #随机取用户ID一个
        urlAPI = "/z01zb_ejyvk/Adminhost/addHost"
        data = {"member_id" : self.hostNum , "remarks" : "自动化添加主持人%d"%self.__randNum}
        re = requests.post(url = self.__url + urlAPI , data = data ,headers = self.__header)
        self.host_id = re.json()["data"]["host_id"]
        assert re.json()["code"] == 200

    def getHostList(self):  # 获取主持人表单
        urlAPI = "/z01zb_ejyvk/Adminhost/getHostList"
        data = {"index" : 1 , "page_size" : 10 }
        re = requests.post(url = self.__url + urlAPI , data = data ,headers = self.__header)
        assert re.json()["data"]["total"] >= 1
        print("获取主持人列表成功，目前主持人总数：%d"%re.json()["data"]["total"])

    def updateHost(self):  #禁用主持人
        urlAPI = "/z01zb_ejyvk/Adminhost/updateHost"
        offData = {"remarks" : "自动修改" , "status" : 1 , "host_id" : self.host_id}
        onData = {"remarks" : "自动修改" , "status" : 2 , "host_id" : self.host_id}
        offRe = requests.post(url = self.__url + urlAPI , data = offData ,headers = self.__header)
        assert offRe.json()["data"]["status"] == 1
        print("主持人ID：%d禁用成功"%self.host_id)
        onRe = requests.post(url=self.__url + urlAPI, data=onData, headers=self.__header)
        assert onRe.json()["data"]["status"] == 2
        print("主持人ID：%d启用成功"%self.host_id)

if __name__ == '__main__':
    ob = hostM()
    ob.addHost()
    ob.getHostList()
    ob.updateHost()