# -*- encoding: utf-8 -*-
"""
@File    : editLive.py
@Time    : 2019/12/31 18:48
@Author  : Liu Yuan
@Author_Email   : document.weite.get@gmail.com
@Software: PyCharm
@Description : 直播管理中，设置直播
"""
from Tools.uploadFiles import upload
import liveManage,hostManager,random
import test_smokeAPI.z01zb_ejyvk.configs as con

class setLive:
    def __init__(self):
        self.__sendPost = liveManage.requestsMoudle()
        self.__getHost_id , self.__getLive_id , self.__getMember_id = \
            hostManager.hostM().addHost() , liveManage.live().addLive() , hostManager.hostM().addHost()

    def getLiveOne(self):   #获取某一单独的直播详情
        re = self.__sendPost.sendPost("/z01zb_ejyvk/Adminlive/getLiveOne" , {"live_id" : self.__getLive_id})
        assert re.json()["data"]["live_id"] == self.__getLive_id
        print("获取直播ID：%d信息成功"%self.__getLive_id)

    def watchEdit(self):    #观看设置  1表示仅限登陆观看，2表示无限制
        offData = {"live_id" : self.__getLive_id , "is_login_read" : 1}
        offRe = self.__sendPost.sendPost("/z01zb_ejyvk/Adminlive/updateLive" , offData)
        assert offRe.json()["data"]["is_login_read"] == 1
        print("观看设置成功：仅限登陆观看")
        onData = {"live_id" : self.__getLive_id , "is_login_read" : 2}
        onRe = self.__sendPost.sendPost("/z01zb_ejyvk/Adminlive/updateLive" , onData)
        assert onRe.json()["data"]["is_login_read"] == 2
        print("观看设置成功：无限制")

    def hostEdit(self):     # 直播主持人设置
        data = {"host_id" : self.__getHost_id , "member_id" : self.__getMember_id , "live_id" : self.__getLive_id}
        re = self.__sendPost.sendPost("/z01zb_ejyvk/Adminlive/addLiveHost" , data)
        assert re.json()["data"]["live_host_id"] != None
        print("直播间设置主持人ID：%d成功"%self.__getHost_id)

    def navigationEdit(self):       # 直播导航栏设置
        # 新增导航栏
        navName = "test%d"%random.randint(1,100)
        addData = {"live_id" : self.__getLive_id , "nav_name" : navName , "sort" : 1 , "leftOrRight" : "right"}
        addRe = self.__sendPost.sendPost("/z01zb_ejyvk/Adminlive/addNav" , addData)
        assert addRe.json()["msg"] == "成功"
        print("新增导航栏名称：%s成功"%navName)
        #获取新增导航栏目录编号
        numData = {"live_id" : self.__getLive_id}
        numRe = self.__sendPost.sendPost("/z01zb_ejyvk/Adminlive/getLiveNavList" , numData)
        getNavId = numRe.json()["data"]["list"][0]["nav_id"]
        assert len(numRe.json()["data"]["list"]) == 1
        print("获取导航栏目编号：%d成功"%getNavId)
        #获取新增导航栏内容
        contentData = {"nav_id" : getNavId}
        contentRe = self.__sendPost.sendPost("/z01zb_ejyvk/Adminlive/getNavContentList" , contentData)
        assert contentRe.json()["msg"] == "获取成功"
        print("获取导航栏目ID：%d内容成功"%getNavId)
        #更改导航栏
        modificationName = "修改的%d"%random.randint(1,100)
        editData = {"nav_id" : getNavId , "nav_name" : modificationName}
        editRe = self.__sendPost.sendPost("/z01zb_ejyvk/Adminlive/updateNav" , editData)
        assert editRe.json()["msg"] == "成功"
        print("更改导航栏：%s成功"%navName)
        # 隐藏导航栏 is_show:1 表示隐藏，2表示显示
        hideData = {"nav_id" : getNavId , "is_show" : 1}
        hideRe = self.__sendPost.sendPost("/z01zb_ejyvk/Adminlive/updateNav" , hideData)
        assert hideRe.json()["msg"] == "成功"
        print("导航栏ID：%d隐藏成功"%getNavId)
        # 取消隐藏导航栏
        showData = {"nav_id" : getNavId , "is_show" : 2}
        showRe = self.__sendPost.sendPost("/z01zb_ejyvk/Adminlive/updateNav" , showData)
        assert showRe.json()["msg"] == "成功"
        print("导航栏ID：%d取消隐藏成功"%getNavId)
        # 添加导航栏图文内容
        contentStr = open("../resources/navContentStr.txt", "r", encoding="utf-8")
        addNavData = {"nav_id" : getNavId , "type" : 1 , "content" : contentStr}
        addNavRe = self.__sendPost.sendPost("/z01zb_ejyvk/Adminlive/addNavContent" , addNavData)
        getNavContentId = addNavRe.json()["data"]["nav_content_id"]
        assert addNavRe.json()["data"]["content"] != None
        print("导航栏新增图文内容成功。")
        # 添加导航栏直播内容
        addNavLiveData = {"nav_id" : getNavId , "type" : 2 , "live_id" : self.__getLive_id}
        addNavLiveRe = self.__sendPost.sendPost("/z01zb_ejyvk/Adminlive/addNavContent" , addNavLiveData)
        getNavLiveId = addNavLiveRe.json()["data"]["nav_content_id"]
        assert addNavLiveRe.json()["data"]["live"] != None
        print("导航栏新增直播内容成功")
        # 获取导航栏被添加内容
        getNavListRe = self.__sendPost.sendPost("/z01zb_ejyvk/Adminlive/getNavContentList" , {"nav_id" : getNavId})
        assert len(getNavListRe.json()["data"]["list"]) >= 2
        print("新增数据后，获取导航栏内容列表成功")
        #修改导航栏图文内容
        deleteNavC = self.__sendPost.sendPost("/z01zb_ejyvk/Adminlive/deleteNavContent" , {"nav_content_id" : getNavContentId})
        deleteNavL = self.__sendPost.sendPost("/z01zb_ejyvk/Adminlive/deleteNavContent" , {"nav_content_id" : getNavLiveId})
        assert deleteNavC.json()["msg"] == "成功"
        assert deleteNavL.json()["msg"] == "成功"
        print("删除导航栏内容成功")
        #删除导航栏
        deleteData = {"nav_id" : getNavId}
        deleteRe = self.__sendPost.sendPost("/z01zb_ejyvk/Adminlive/deleteNav" , deleteData)
        assert deleteRe.json()["msg"] == "成功"
        print("删除导航栏目ID：%d成功"%getNavId)

    def setLiveArg(self):   # 设置直播参数
        data = {"push_url" : con.push_url , "hls_url" : con.hls_url , "rtmp_url" : con.rtmp_url , "hdl_url" : con.hdl_url , "live_id" : self.__getLive_id}
        re = self.__sendPost.sendPost("/z01zb_ejyvk/Adminlive/updateLive" , data)
        assert re.json()["data"]["live_id"] == self.__getLive_id
        print("直播参数设置，保存功能正常。")

    def setShare(self):     # 直播分享设置
        setData = {"share_title" : "自动化添加分享标题" , "share_introduce" : "自动化添加分享描述" ,
                "share_img_url" : upload().uploadImg("../resources/demoImg.png") ,
                "live_id" : self.__getLive_id}
        setRe = self.__sendPost.sendPost("/z01zb_ejyvk/Adminlive/updateLive" , setData)
        assert setRe.json()["data"]["share_title"] != None

        modificationData = {"share_title" : "自动化修改后的分享标题" , "share_introduce" : "自动化修改后的分享描述" ,
                "share_img_url" : upload().uploadImg("../resources/demoImg01.png") ,
                "live_id" : self.__getLive_id}
        modificationRe = self.__sendPost.sendPost("/z01zb_ejyvk/Adminlive/updateLive" , modificationData)
        assert modificationRe.json()["data"]["share_title"] != None
        print("自动化设置、修改分享成功")

    def watchLive(self):    # 设置观看直播
        data = {"read_init_num" : 100 , "read_minute_add_num" : 100 , "read_add_rate" : 100 ,
                "like_init_num" : 100 , "like_minute_add_num" : 100 , "like_add_rate" : 100 ,
                "live_id" : self.__getLive_id}
        re = self.__sendPost.sendPost("/z01zb_ejyvk/Adminlive/updateLive" , data)
        assert re.json()["data"]["like_minute_add_num"] == 100
        print("自动化设置直播观看数据成功")

    def replayLive(self):   # 设置直播回放录像
        #   获取回放录像列表
        getListData = {"page" : 1 , "page_size" : 10 , "live_id" : self.__getLive_id}
        getList = self.__sendPost.sendPost("/z01zb_ejyvk/Adminplayback/getPlaybackList" , getListData)
        assert getList.json()["msg"] == "获取成功"
        print("获取回放录像列表成功")
        #   新建回放录像
        addData = {"title" : "自动化添加标题" , "sort" : 4 ,
                   "cover_img_url" : upload().uploadImg("../resources/demoImg01.png") ,
                   "video_url" : upload().uploadImg("../resources/demoVideo01.mp4") ,
                   "live_id" : self.__getLive_id}
        addReplay = self.__sendPost.sendPost("/z01zb_ejyvk/Adminplayback/addPlayback" , addData)
        getBackId = addReplay.json()["data"]["playback_id"]
        assert addReplay.json()["data"]["create_time"] != None
        #   编辑直播
        setReplayData = {"title" : "自动化修改标题" , "sort" : 4 ,
                         "cover_img_url" : upload().uploadImg("../resources/demoImg.png") ,
                         "video_url" : upload().uploadImg("../resources/demoVideo.mp4") ,
                         "live_id" : self.__getLive_id , "playback_id" : getBackId}
        setReplay = self.__sendPost.sendPost("/z01zb_ejyvk/Adminplayback/updatePlayback" , setReplayData)
        assert setReplay.json()["data"]["update_time"] != None
        print("编辑、新建回放录像成功")

    def dataStatistics(self):   #直播数据统计
        #  获取观看人次列表
        data = {"live_id" : self.__getLive_id , "index" : 1 , "page_size" : 10}
        getViewerList = self.__sendPost.sendPost("/z01zb_ejyvk/Adminlive/getReadLogList" , data)
        assert getViewerList.status_code == 200
        #  获取点赞列表
        getLikeList = self.__sendPost.sendPost("/z01zb_ejyvk/Adminlive/getLikeList" , data)
        assert getLikeList.status_code == 200
        #  获取聊天列表
        getChatList = self.__sendPost.sendPost("/z01zb_ejyvk/Adminlive/getChatList" , data)
        assert getChatList.status_code == 200
        print("获取观看人次、点赞、聊天列表成功")

    def run(self):
        self.getLiveOne() , self.watchEdit() , self.hostEdit() , self.navigationEdit() , \
        self.setLiveArg() , self.setShare() , self.watchLive() , self.replayLive() , self.dataStatistics()


# if __name__ == '__main__':
#     ob = setLive()
#     ob.getLiveOne()
#     ob.watchEdit()
#     ob.hostEdit()
#     ob.navigationEdit()
#     ob.setLiveArg()
#     ob.setShare()
#     ob.watchLive()
#     ob.replayLive()
#     ob.dataStatistics()