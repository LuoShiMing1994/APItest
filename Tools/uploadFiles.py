# -*- encoding: utf-8 -*-
"""
@File    : uploadFiles.py
@Time    : 2019/12/19 11:42
@Author  : Liu Yuan
@Author_Email   : document.weite.get@gmail.com
@Software: PyCharm
@Description : 上传文件
"""

import requests
from test_smokeAPI.z01zb_ejyvk import configs as con

class upload:
    def __init__(self):
        self.__url = con.url

    def uploadImg(self,filesPath) :
        header = {"token" : "89F2E50EE4C2DDE0023CDCF858C1E5C3"}
        files = {"file": open(filesPath, "rb")}
        re = requests.post(url= self.__url + "/z01zb_ejyvk/Adminlive/imgUpload", files= files,headers= header)
        return re.json()["data"]["all_path"]

# if __name__ == '__main__':
#     ob = upload()
#     ob.uploadImg("/z01zb_ejyvk/Adminlive/imgUpload")