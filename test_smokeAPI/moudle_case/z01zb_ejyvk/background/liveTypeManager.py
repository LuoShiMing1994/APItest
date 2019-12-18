# -*- encoding: utf-8 -*-
"""
@File    : liveliveBaseEdit.py
@Time    : 2019/12/13 15:24
@Author  : Liu Yuan
@Author_Email   : document.weite.get@gmail.com
@Software: PyCharm
@Description : 后台直播管理频道
"""
import requests,json,random,time,os
from test_smokeAPI.moudle_case.z01zb_ejyvk import configs as con

class liveBaseEdit:
    def __init__(self):
        self.sess = requests.session()  #获取一个session对象
        self.__url , self.__header= con.url , con.header
        self.__randNum = random.randint(1,100000)
    def addChannel(self): #新建频道分类
        urlAPI = "/z01zb_ejyvk/Adminchannel/addChannel"
        data = {"channel_name" : "test%d"%self.__randNum , "channel_dec" : "自动化接口测试添加" , "status" : "2"}
        re = requests.post(url = self.__url + urlAPI , data = data , headers = self.__header)
        self.__currencyNameValue , self.__currencyIdValue , self.__currencyStatus = re.json()["data"]["channel_name"] , \
                                                            re.json()["data"]["channel_id"] , re.json()["data"]["status"]
        assert "自动化接口测试添加" in re.text
        print("频道分类新建成功：" + "test%d"%self.__randNum)

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
    #
    def addLive(self):  #新增直播
        urlAPI = "/z01zb_ejyvk/Adminlive/addLive"
        upload = "/z01zb_ejyvk/Adminlive/imgUpload"
        imgFiles = {"file" : open(r"D:\devImg\LOGO.png" , "rb") ,
                    "Content-Disposition" : "form-data" ,
                    "Content-Type" : "image/png" ,
                    "filename" : "LOGO.png" }
        requests.post(url = self.__url + upload , headers = self.__header , files = imgFiles)
        # with open(r"C:\Users\lyy\PycharmProjects\TenmaLy\test_smokeAPI\moudle_case\z01zb_ejyvk\background\str200.txt" , "r" ,
        #      encoding = "utf-8") as f :
        #     contentStr200 = f.read()
        # data = {"title" : "接口添加接口添加接口添加接口添接口添加接口添加接口添加接口添" , "cover_img_url" : "" ,
        #         "start_time" : time.time() , "introduce" : contentStr200 , "channel_id" : self.__currencyIdValue ,
        #         "notice_video_url" : ""}

if __name__ == '__main__':
    ob = liveBaseEdit()
    # ob.addHost()
    # ob.getHostList()
    # ob.updateHost()
    ob.addLive()