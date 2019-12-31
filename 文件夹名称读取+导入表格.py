# Users/尹茂金/PycharmProjects
# !-*- coding:utf-8 -*-
# !@time:2019/12/22,17:51
# !@Author: 尹茂金
# !@File:collect.py
# 56行 # 存放路径+文件名  ./mydata.xls意思是存放到当前执行文件路径下的mydata.xls文件里
# 60行 # 选择要整理的文件的父文件夹路径
import os
import xlwt


def file_dirs(file_dir):
    for root, dirs, files in os.walk(file_dir):
        # root   当前目录路径
        # dirs   当前路径下所有子目录
        # files  当前路径下所有非目录子文件
        return dirs


def data_save(dict_stu):
    xls = xlwt.Workbook()  # 新建工作簿
    sht1 = xls.add_sheet('Sheet1', cell_overwrite_ok=True)  # 增加工作表
    # 添加字段
    sht1.write(0, 0, '序号')
    sht1.write(0, 1, '学号')
    sht1.write(0, 2, '姓名')
    sht1.write(0, 3, '实操一')
    sht1.write(0, 4, '实操二')
    sht1.write(0, 5, '实操三')
    sht1.write(0, 6, '实操四')
    sht1.write(0, 7, '均值')
    # 给字段中加值   考虑使用循环
    for i, j in enumerate(dict_stu.keys()):
        sht1.write(i+1, 0, i+1)
        sht1.write(i+1, 1, j[0])
        sht1.write(i+1, 2, j[1])
        a = 0
        for k, s in enumerate(tuple(dict_stu[j[0], j[1]])):
            # print(s)
            if s == "操作一":
                sht1.write(i + 1, 3, tuple(dict_stu[j[0], j[1]])[k+1])
                a += int(tuple(dict_stu[j[0], j[1]])[k+1])
            elif s == "操作二":
                sht1.write(i + 1, 4, tuple(dict_stu[j[0], j[1]])[k+1])
                a += int(tuple(dict_stu[j[0], j[1]])[k + 1])
            elif s == "操作三":
                sht1.write(i + 1, 5, tuple(dict_stu[j[0], j[1]])[k+1])
                a += int(tuple(dict_stu[j[0], j[1]])[k + 1])
            elif s == "操作四":
                sht1.write(i + 1, 6, tuple(dict_stu[j[0], j[1]])[k+1])
                a += int(tuple(dict_stu[j[0], j[1]])[k + 1])
            sht1.write(i + 1, 7, a/4)

    xls.save('./mydata.xls')  # 存放路径+文件名  ./mydata.xls意思是存放到当前执行文件路径下的mydata.xls文件里


def main():
    dirs = r"C:\Users\尹茂金\Desktop\新建文件夹 (2)"  # 选择要整理的文件的父文件夹路径
    dir_first = file_dirs(dirs)
    dir_second = []
    for i in dir_first:
        dir_second.append(file_dirs(dirs + "\\" + str(i)))
        # print(dir_second)
        for k in range(len(dir_second)):
            if "重考" in dir_second[k]:
                b = file_dirs(dirs + "\\" + str(i) + "\\" + "重考")
                list2 = []
                for b1 in b:
                    list2.append(b1)
                dir_second.append(list2)
                dir_second[k].remove("重考")
    # print(dir_second)
    list1 = []
    for a1 in dir_second:
        for strs in a1:
            list1.append(strs.split("+"))
    # print(list1)  # 检验列表
    # data_save(list1)
    dict_data = {}
    for i in list1:
        dict_data[i[2], i[3], i[0]] = i[4]
    list_stu = []
    for i in dict_data.items():
        list_stu.append(i)
    #  list_stu[a][1]  表示分数
    #  list_stu[a][0][0]  表示学号
    #  list_stu[a][0][1]  表示姓名
    #  list_stu[a][0][2]  表示实操科目
    dict_stu = {}
    for i in range(len(list_stu)):
        if (list_stu[i][0][0], list_stu[i][0][1]) in dict_stu.keys():
            dict_stu[list_stu[i][0][0], list_stu[i][0][1]] = \
                dict_stu[list_stu[i][0][0], list_stu[i][0][1]] + \
                (list_stu[i][0][2], list_stu[i][1])
        else:
            dict_stu[list_stu[i][0][0], list_stu[i][0][1]] = (list_stu[i][0][2], list_stu[i][1])
    # print(dict_stu)
    data_save(dict_stu)
    print("Saved successfully!")


if __name__ == '__main__':
    main()
