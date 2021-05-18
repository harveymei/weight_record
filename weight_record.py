#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/5/14 5:05 下午
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: weight_record.py
# @IDE     : PyCharm
# @GitHub  : https://github.com/harveymei/

"""
Python Cook Book 参考章节
Json操作 6.2
文件操作 5.5

Python Crash Book 参考章节

当前待完善特性：
1，matplotlib图形中中文字符的支持
2，判断用户输入非法字符的异常处理
3，根据自动计算的BMI值，合并绘图
4，提示符显示文件中已录入最新数据
"""

# 检测文件是否存在
import os
import csv
import datetime
from matplotlib import pyplot as plt

# 检查数据文件是否存在，不存在则创建
filename = 'weight_record.csv'
if not os.path.exists(filename):
    with open(filename, 'wt') as f:
        f.write('Date,Height,Weight,BMI\n')


# 定义用户录入函数
# https://docs.python.org/3/library/functions.html#isinstance
# 应当判断用户输入的有效性
def data_input():
    # 获取当前系统时间数据 current_date current_time
    current_system_date = datetime.datetime.now().strftime('%Y-%m-%d')

    # 获取用户输入输入
    current_date = input("请输入当前日期数值或直接按回车键使用默认数值: " + '(' + current_system_date + ') ')
    if current_date == '':
        current_date = current_system_date

    current_height = input("请输入当前身高数值或直接按回车键使用默认数值(m): (1.72)")
    if current_height == '':
        current_height = 1.72

    current_weight = float(input("请输入当前体重数值(kg): "))

    current_bmi = round(current_weight / (current_height ** 2), 2)

    # 拼接数据
    new_data = current_date + ',' + str(current_height) + ',' + str(current_weight) + ',' + str(current_bmi) + '\n'

    # 写入文件
    with open(filename, 'a') as f_object:
        f_object.write(new_data)

    print("录入完成. ")
    key = input("按c键继续或按q键退出. ")
    if key == 'c':
        data_input()
    elif key == 'q':
        exit()
    else:
        print("错误输入")


def data_output():
    """
    数据输出函数
    """
    with open(filename) as f_object:
        reader = csv.reader(f_object)
        header_row = next(reader)  # 读取文件头（首行）

        dates, weights = [], []
        for row in reader:
            date = row[0]
            weight = float(row[2])  # 将遍历到的字符串数值转换为浮点数

            dates.append(date)
            weights.append(weight)

    # 函数figure()用于指定图表的宽度、高度、分辨率和背景色
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, weights, c='red')

    plt.title("Weight Record 2021", fontsize=24)
    plt.xlabel("", fontsize=16)
    fig.autofmt_xdate()  # 绘制斜的日期标签
    plt.ylabel("Weight (Kg)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=8)

    # plt.show()
    saved_file = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    plt.savefig(saved_file + '.png')


# 打印信息，提示用户操作
print("请选择将要执行的操作:\n"
      "1) 录入新数据\n"
      "2) 查看可视化数据")

# 提示用户输入并判断输入有效性
option = input("请输入编号并按回车键: ")
if option == '1':
    print("开始数据录入……")
    data_input()
elif option == '2':
    print("开始数据输出……")
    data_output()
else:
    print("输入错误")
