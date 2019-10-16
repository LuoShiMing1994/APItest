import xlrd
class get_xlsx:
    def __init__(self,data_url):
        xlsx_read = xlrd.open_workbook(data_url)  # 给予文件路径
        self.__table = xlsx_read.sheet_by_index(0)  # 获取文件下标为0的所有数据,现在是个对象
        self.__nrows = self.__table.nrows     #获取表格__table的总行数
        self.__ncols = self.__table.ncols     #获取表格__table的总列数
        self.__titles = self.__table.row_values(0)    #获取表格__table的第一行的列名
        self.__data_xlsx = []
    def get_data_list(self):
        for i in range(1,self.__nrows) :
            values = self.__table.row_values(i)    #__table表格内的每一行的数据
            dic = {}
            for k in range(self.__ncols) :
                dic[self.__titles[k]] = values[k]   #把每一行数据拿出来以字典的方式储存
            self.__data_xlsx.append(dic)
        return self.__data_xlsx     #返回值是一个以字典为元素的列表


    #     pass
    #     # url = r"../case/tenmaMoudle/babyWarehouseData/demo1.xlsx"
    #     # data = get_xlsx(url).get_data_list()
    #     # print(data)