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
from test_smokeAPI.moudle_case.z01zb_ejyvk import configs as con

def uploadImg() :
    header = {
        "Content-Type": "multipart/form-data",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "token": "3104EB9D1C7C2F9688074EA23D6D5CBE"
    }
    url = con.url
    files = {"file" : ("3.jpg" , open(r"D:/" , "rb") , "image/png" , {})}
    re = requests.post(url,files=files,headers=header)



if __name__ == '__main__':
    uploadImg()