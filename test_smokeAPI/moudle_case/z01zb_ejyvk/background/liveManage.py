# -*- encoding: utf-8 -*-
"""
@File    : liveManage.py
@Time    : 2019/12/30 19:10
@Author  : Liu Yuan
@Author_Email   : document.weite.get@gmail.com
@Software: PyCharm
@Description : 直播管理
"""

import requests,time
from test_smokeAPI.moudle_case.z01zb_ejyvk import configs as con
from Tools import uploadFiles
class live():
    def __init__(self):
        self.__url, self.__header = con.url, con.header
        uploadAPI = "/z01zb_ejyvk/Adminlive/imgUpload"
    def addLive(self):
        getImgURL = uploadFiles.upload().uploadImg("/z01zb_ejyvk/Adminlive/imgUpload")