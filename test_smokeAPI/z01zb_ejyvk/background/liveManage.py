# -*- encoding: utf-8 -*-
"""
@File    : liveManage.py
@Time    : 2019/12/30 19:10
@Author  : Liu Yuan
@Author_Email   : document.weite.get@gmail.com
@Software: PyCharm
@Description : 直播管理模块
"""

import time,random
from Tools import uploadFiles
from test_smokeAPI.z01zb_ejyvk.background import liveTypeManager
from Tools.requestPack import requestsMoudle

class live():
    def __init__(self):
        pass

    def addLive(self):  #新建一个直播
        self.__randomN = random.randint(1, 100000)
        getImgURL = uploadFiles.upload().uploadImg("demoImg.png")
        getVideoURL = uploadFiles.upload().uploadImg(r"D:\devImg\demoVideo.mp4")
        self.__getChannelID = liveTypeManager.liveBaseEdit().addChannel()
        getIntroduce = open("str200.txt" , "r" , encoding= "utf-8")
        self.__editTitle = "接口自动化添加接口自动化添加接口自动化添加%d"%self.__randomN
        data = {"title" : self.__editTitle , "cover_img_url" : getImgURL ,
                "start_time" : int(time.time()) , "channel_id" : self.__getChannelID , "introduce" : getIntroduce.read(),
                "notice_video_url" : getVideoURL , "live_screen" : 2}
        responesObject = requestsMoudle().sendPost("/z01zb_ejyvk/Adminlive/addLive" , data)
        self.__getLive_id = responesObject.json()["data"]["live_id"]
        assert responesObject.json()["msg"] == "成功"
        print("新建直播名称成功：%s"%self.__editTitle)

    def siftLive(self) :  #搜索新建的直播
        descData = {"input" : self.__editTitle , "index" : 1 , "page_size" : 10 , "status" : 1 ,
                "is_online" : 1 , "channel_id" : self.__getChannelID , "sort" : "desc"}
        descRe = requestsMoudle().sendPost("/z01zb_ejyvk/Adminlive/getLiveList" , descData)
        assert descRe.json()["data"]["all_count"] == 1
        print("按照创建时间降序筛选直播成功")
        ascData = {"input" : self.__editTitle , "index" : 1 , "page_size" : 10 , "status" : 1 ,
                "is_online" : 1 , "channel_id" : self.__getChannelID , "sort" : "asc"}
        ascRe = requestsMoudle().sendPost("/z01zb_ejyvk/Adminlive/getLiveList" , ascData)
        assert ascRe.json()["data"]["all_count"] == 1
        print("按照创建时间升序筛选直播成功")

    def updateLive(self):   #上下架新建的直播"is_online" 1下架，2上架
        onData = {"live_id" : self.__getLive_id , "is_online" : 2 }
        re = requestsMoudle().sendPost("/z01zb_ejyvk/Adminlive/updateLive" , onData)
        assert re.json()["data"]["is_online"] == 2
        print("新建的直播上架成功")
        offData = {"live_id" : self.__getLive_id , "is_online" : 1 }
        re = requestsMoudle().sendPost("/z01zb_ejyvk/Adminlive/updateLive", offData)
        assert re.json()["data"]["is_online"] == 1
        print("新建的直播下架成功")

    def startLive(self):    #开启/关闭直播
        # 只有上架的直播才能开启或关闭
        requireOnData = {"live_id" : self.__getLive_id , "is_online" : 2 }
        requestsMoudle().sendPost("/z01zb_ejyvk/Adminlive/updateLive", requireOnData)
        onData = {"live_id" : self.__getLive_id , "status" : 2 }
        re = requestsMoudle().sendPost("/z01zb_ejyvk/Adminlive/updateLive",onData)
        assert re.json()["msg"] == "成功"
        print("启动直播成功")
        offData = {"live_id" : self.__getLive_id , "status" : 3 }
        re = requestsMoudle().sendPost("/z01zb_ejyvk/Adminlive/updateLive",offData)
        assert re.json()["msg"] == "成功"
        print("关闭直播成功")
        #下架直播，恢复状态
        requireOffData = {"live_id" : self.__getLive_id , "is_online" : 1 }
        requestsMoudle().sendPost("/z01zb_ejyvk/Adminlive/updateLive", requireOffData)




if __name__ == '__main__':
    ob = live()
    ob.addLive()
    ob.siftLive()
    ob.updateLive()
    ob.startLive()