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

# 导入Python内置模块和外部模块
import os
import csv
import datetime
from matplotlib import pyplot as plt

# 检查数据文件是否存在，不存在则创建
filename = 'weight_record.csv'
if not os.path.exists(filename):
    with open(filename, 'wt') as f:
        f.write('Date,Height,Weight,BMI\n')


def data_input():
    """
    数据录入函数
    """
    # 获取当前系统时间
    system_date = datetime.datetime.now().strftime('%Y-%m-%d')  # 日期对象转换为日期字符串

    # 获取用户输入输入
    current_date = input("请输入当前日期数值或直接按回车键使用默认数值: " + "(" + system_date + ") ")
    if current_date == '':
        current_date = system_date

    current_height = float(input("请输入当前身高数值或直接按回车键使用默认数值(m): (1.72) "))
    if current_height == '':
        current_height = 1.72

    current_weight = float(input("请输入当前体重数值(kg): "))

    current_bmi = round(current_weight / (current_height ** 2), 2)

    # 拼接数据
    new_data = current_date + ',' + str(current_height) + ',' + str(current_weight) + ',' + str(current_bmi) + '\n'

    # 写入文件，追加写模式
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

        dates, weights = [], []  # 定义空列表以存储遍历到的数据
        for row in reader:  # 从第二行开始遍历
            # 当字符串日期直接放入列表时，将绘制所有日期标签
            # date = row[0]
            # 当字符串日期转换为日期对象后，将会随数据增加和图表宽度自适应绘制日期标签
            date = datetime.datetime.strptime(row[0], '%Y-%m-%d')  # 字符串日期转换为日期对象
            weight = float(row[2])  # 将遍历到的字符串数值转换为浮点数

            dates.append(date)
            weights.append(weight)

    # 函数figure()用于指定图表的宽度、高度、分辨率和背景色
    fig = plt.figure(dpi=128, figsize=(10, 6))
    # 绘图
    plt.plot(dates, weights, c='red')  # 分别传入x坐标和y坐标值列表

    # 设置标题，x和y轴标签属性
    plt.title("Weight Records From 2021", fontsize=24)
    plt.xlabel("", fontsize=16)
    # https://matplotlib.org/stable/api/figure_api.html?highlight=autofmt_xdate#matplotlib.figure.Figure.autofmt_xdate
    fig.autofmt_xdate()  # 绘制斜的日期标签，默认参数值为右对齐旋转30度
    plt.ylabel("Weight (Kg)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    # plt.show()
    saved_file = datetime.datetime.now().strftime('%Y%m%d%H%M%S')  # 日期对象转换为日期字符串
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
