# -*- encoding: utf-8 -*-
"""
@File    : editPointStatus.py
@Time    : 2019/11/27 14:35
@Author  : Liu Yuan
@Author_Email   : document.weite.get@gmail.com
@Software: PyCharm
@Description : 用于运营综合体批量上下架shop
"""

import requests,json

class edit():
    def getOn(self,urlAdress,num):
        counts = num
        while True :
            counts += 1
            if 21 < counts < 79:
                headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                           "token": "9A2751F41467DE631E2A9B942C851C4C"}
                data = {"id": "%d"%counts, "status": "1"}
                re = requests.post(url=urlAdress,data=data,headers=headers)
                print(re.status_code + counts)
            else :
                break
        print("上架完成")

    def getUp(self,urlAdress,num):
        pass

if __name__ == '__main__':
    set = edit()
    url = "http://mistest.tianma3600.com:39080/operate_platform/Pointshop/addEdit"
    actionNum =22
    set.getOn(url,actionNum)


