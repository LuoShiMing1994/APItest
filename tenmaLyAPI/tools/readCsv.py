import os
class get_csv: # 把csv文件转换为字典存储
    def __init__(self,data_url):    #参数为相对路径
        with open(os.path.abspath(data_url), "r") as csv_file:
            self.__csv_read = csv_file.readlines()
            self.__csv_content = self.__csv_read[0].strip().split(",")  # 取出了表格所有的列名
            self.__csv_data = []
    def get_data_list(self):
            for i in range(1,len(self.__csv_read)) : #循环用于取出所有的内容,把数据以行的形式取出，再拿去给字典赋值
                row = self.__csv_read[i].strip().split(",")
                dict = {}
                for j in range(len(self.__csv_content)): #把外循环每一行的数据取出来放进字典里面
                    dict[self.__csv_content[j]] = row[j]
                self.__csv_data.append(dict)
            return self.__csv_data

if __name__ == '__main__':
    # url = r"../case/tenmaMoudle/babyWarehouseData/demo.csv"
    # data = get_csv(url).get_data_list()
    # print(data)
    pass
