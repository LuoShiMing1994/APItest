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
    def getOn(self,urlAdress,num,statusN):
        counts = num
        while True :
            counts += 1
            if 1 <= counts <= 100:
                headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                           "token": "9A2751F41467DE631E2A9B942C851C4C"}
                data = {"id": "%d"%counts, "status": "%d"%statusN}
                re = requests.post(url=urlAdress,data=data,headers=headers)
                print(re.status_code + counts)
            else :
                break
        print("已全部上下架完成")

if __name__ == '__main__':
    set = edit()
    url = "http://mistest.tianma3600.com:39080/operate_platform/Pointshop/addEdit"
    URLAC = "http://mistest.tianma3600.com:39080/operate_platform/Activity/addEdit"
    actionNum =0
    status = 1 #0表示下架，1表示上架
    set.getOn(URLAC,actionNum,status)
    # set.getDown(url,actionNum)

