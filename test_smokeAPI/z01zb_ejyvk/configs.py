# -*- encoding: utf-8 -*-
"""
@File    : configs.py
@Time    : 2019/12/16 20:10
@Author  : Liu Yuan
@Author_Email   : document.weite.get@gmail.com
@Software: PyCharm
@Description : 配置文件
"""
import random

url = "http://dev.360tianma.com"
header = {
         "Content-Type":"application/x-www-form-urlencoded",
         "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
         "token":"89F2E50EE4C2DDE0023CDCF858C1E5C3"
         }
randomN = random.randint(1, 100000)