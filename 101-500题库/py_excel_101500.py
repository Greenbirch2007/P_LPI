# coding=utf-8


import xlrd


def cut_list(one_data_list, colnum=10):
    '''
    将一维的列表转化为矩阵形式
    '''
    res_list = []
    for i in range(0, len(one_data_list), colnum):
        res_list.append(one_data_list[i:i + colnum])
    return res_list
def read_xlrd(excelFile):
    data = xlrd.open_workbook(excelFile)
    table = data.sheet_by_index(0)
    dataFile = []
    for rowNum in range(table.nrows):
        dataFile.append(table.row_values(rowNum))

    # if 去掉表头
       # if rowNum => 0:

    return dataFile


if __name__ == '__main__':
    excelFile = '/home/w/P_LPI/101-500题库/l101_500answer.xlsx'
    # 先把单表的名字容器给弄出来
    # names_list = set()
    new_list = []
    for item in read_xlrd(excelFile=excelFile):

        new_list.append(item)
    l = cut_list(new_list,colnum=10)
    for item in l:
        print(item)


    #     names_list.add(item[0])
    # full_items = read_xlrd(excelFile=excelFile)
    # for single_name  in names_list:
    #     one_list = []
    #     one_list.append(single_name)
    #     for item in full_items:
    #         if single_name == item[0]:
    #             one_list.append(item[1])
    #         else:
    #             pass


