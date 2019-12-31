# Users/尹茂金/PycharmProjects
# !-*- coding:utf-8 -*-
# !@time:2019/12/22,11:54
# !@Author: 尹茂金
# !@File:dir.py
import os
import xlwt


def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        # root   当前目录路径
        # dirs   当前路径下所有子目录
        # files  当前路径下所有非目录子文件
        return dirs


def data_save(lists):
    xls = xlwt.Workbook()  # 新建工作簿
    sht1 = xls.add_sheet('Sheet1', cell_overwrite_ok=True)  # 增加工作表
    # 添加字段
    sht1.write(0, 0, '序号')
    sht1.write(0, 1, '实践科目')
    sht1.write(0, 2, '班级')
    sht1.write(0, 3, '学号')
    sht1.write(0, 4, '姓名')
    sht1.write(0, 5, '自评分')
    # 给字段中加值   考虑使用循环
    for i in range(1, len(lists) + 1):
        for j in range(5):
            sht1.write(i, 0, i)  # 填入序号
            sht1.write(i, j + 1, str(lists[i - 1][j]))  # 填入值

    xls.save('./mydata.xls')  # 存放路径+文件名  ./mydata.xls意思是存放到当前执行文件路径下的mydata.xls文件里


def main():
    dirs = r"C:\Users\尹茂金\Desktop\新建文件夹 (2)"  # 选择要整理的文件的父文件夹路径
    a = file_name(dirs)
    if "重修" in a:
        b = file_name(dirs + "\\重修")
        for b1 in b:
            a.append(b1)
        a.remove("重修")
    list1 = []
    for strs in a:
        list1.append(strs.split("+"))
    print(list1)  # 检验列表
    # data_save(list1)


if __name__ == '__main__':
    main()
