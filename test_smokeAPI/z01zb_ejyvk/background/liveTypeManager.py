# -*- encoding: utf-8 -*-
"""
@File    : liveliveBaseEdit.py
@Time    : 2019/12/13 15:24
@Author  : Liu Yuan
@Author_Email   : document.weite.get@gmail.com
@Software: PyCharm
@Description : 直播频道管理
"""
import requests, random
from test_smokeAPI.z01zb_ejyvk import configs as con

class liveBaseEdit:
    def __init__(self):
        self.sess = requests.session()  #获取一个session对象
        self.__url , self.__header= con.url , con.header
        self.__randNum = random.randint(1,100000)

    def addChannel(self):  #新建频道分类
        urlAPI = "/z01zb_ejyvk/Adminchannel/addChannel"
        data = {"channel_name" : "test%d"%self.__randNum , "channel_dec" : "自动化接口测试添加" , "status" : "2"}
        re = requests.post(url = self.__url + urlAPI , data = data , headers = self.__header)
        self.__currencyNameValue , self.__currencyIdValue , self.__currencyStatus = re.json()["data"]["channel_name"] , \
                                                            re.json()["data"]["channel_id"] , re.json()["data"]["status"]
        assert "自动化接口测试添加" in re.text
        print("频道分类新建成功：" + "test%d"%self.__randNum)
        return self.__currencyIdValue

    def offLiveType(self): #禁用直播频道
        urlAPI = "/z01zb_ejyvk/Adminchannel/updateChannel"
        dataOff = {"channel_id" : self.__currencyIdValue , "status" : 1}
        re = requests.post(url= self.__url + urlAPI , data= dataOff , headers= self.__header)
        assert "成功" in re.text
        print("频道禁用成功，频道ID：%d"%self.__currencyIdValue)

    def onLiveType(self):   #启用直播频道
        urlAPI = "/z01zb_ejyvk/Adminchannel/updateChannel"
        dataOn = {"channel_id" : self.__currencyIdValue , "status" : 2}
        re = requests.post(url=self.__url + urlAPI, data=dataOn, headers=self.__header)
        assert "成功" in re.text
        print("频道解除禁用成功，频道ID：%d"%self.__currencyIdValue)

    def updateChannel(self):     #编辑频道分类
        urlAPI = "/z01zb_ejyvk/Adminchannel/updateChannel"
        data = {"channel_name" : "编辑后标题%d"%self.__randNum , "channel_dec" : "编辑后描述%d"%self.__randNum ,
                "status" : self.__currencyStatus , "channel_id" : self.__currencyIdValue}
        re = requests.post(url= self.__url + urlAPI , data=data , headers= self.__header)
        assert "编辑后标题%d"%self.__randNum in re.text
        print("频道标题编辑成功为: " + "编辑后标题%d"%self.__randNum)

    def getChannelList(self):   #搜索频道
        urlAPI = "/z01zb_ejyvk/Adminchannel/getChannelList"
        data = {"input" : "编辑后标题%d"%self.__randNum , "status" : 2}
        re = requests.post(url= self.__url + urlAPI , data= data , headers = self.__header)
        count = re.json()["data"]["total"]
        assert count == 1
        print("搜索频道%s成功"%"编辑后标题%d"%self.__randNum)

    def run(self):
        self.addChannel() , self.offLiveType() , self.onLiveType() , self.updateChannel() , self.getChannelList()
# if __name__ == '__main__':
#     ob = liveBaseEdit()
#     ob.addChannel()
#     ob.offLiveType()
#     ob.onLiveType()
#     ob.updateChannel()
#     ob.getChannelList()