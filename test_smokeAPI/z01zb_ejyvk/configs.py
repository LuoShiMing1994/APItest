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
     "token":"80895744A2BA74B7942A7EBC5DB7329A"
     }
randomN = random.randint(1, 100000)
push_url = "rtmp://pili-publish.gxyl.tianma3600.com/gxyl/B2FE105B5DAE262D5B17C1EDD9EF2FD3?e=1577967766&token" \
           "=N059HgeD60hpIlYPzY0ukub3--vwDYDiZJh1-tbM:l9syCEm71s1o0o4z6avAI2VznjA="
hls_url = "http://pili-live-hls.gxyl.tianma3600.com/gxyl/B2FE105B5DAE262D5B17C1EDD9EF2FD3.m3u8"
rtmp_url = "rtmp://pili-live-hls.gxyl.tianma3600.com/gxyl/B2FE105B5DAE262D5B17C1EDD9EF2FD3"
hdl_url = "http://pili-live-hls.gxyl.tianma3600.com/gxyl/B2FE105B5DAE262D5B17C1EDD9EF2FD3.flv"