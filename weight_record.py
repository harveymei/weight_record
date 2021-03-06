#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/5/14 5:05 下午
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: weight_record.py
# @IDE     : PyCharm
# @GitHub  : https://github.com/harveymei/

"""
参考书目：
Python Cook Book
Python Crash Course

功能特性：
1，引入os模块检查文件是否存在
2，引入csv模块读写csv格式文件
3，引入datetime模块处理时间类型与字符串类型日期的格式化转换
4，根据录入的身高及体重数据自动计算的BMI值
5，引入font_manager模块，处理中文字符显示
6，用户操作选项菜单函数，退出主程序通过菜单退出
"""

# 导入Python内置模块和外部模块
import os
import csv
import datetime
from matplotlib import pyplot as plt
import matplotlib.font_manager as mfm

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

    current_height = input("请输入当前身高数值或直接按回车键使用默认数值(m): (1.72) ")
    if current_height == '':
        current_height = 1.72

    current_weight = input("请输入当前体重数值(kg): ")

    current_bmi = round(float(current_weight) / (current_height ** 2), 2)

    # 拼接数据
    new_data = current_date + ',' + str(current_height) + ',' + current_weight + ',' + str(current_bmi) + '\n'

    # 写入文件，追加写模式
    with open(filename, 'a') as f_object:
        f_object.write(new_data)

    print("录入完成. ")
    key = input("按c键继续或按q键退出. ")
    if key == 'c':
        data_input()
    elif key == 'q':
        # exit(） # 由直接退出主程序，改为调用启动菜单退出主程序
        menu()
    else:
        print("错误输入")


def data_output():
    """
    数据输出函数
    """
    with open(filename) as f_object:
        reader = csv.reader(f_object)
        header_row = next(reader)  # 读取文件头（首行）

        date_list, weight_list, bmi_list = [], [], []  # 定义空列表以存储遍历到的数据
        for row in reader:  # 从第二行开始遍历
            # 当字符串日期直接放入列表时，将绘制所有日期标签
            # date = row[0]
            # 当字符串日期转换为日期对象后，将会随数据增加和图表宽度自适应绘制日期标签
            date = datetime.datetime.strptime(row[0], '%Y-%m-%d')  # 字符串日期转换为日期对象
            weight = float(row[2])  # 将遍历到的字符串数值转换为浮点数
            bmi = float(row[-1])

            date_list.append(date)
            weight_list.append(weight)
            bmi_list.append(bmi)
            last_date = datetime.datetime.strftime(date_list[-1], '%Y-%m-%d')
            last_bmi = str(bmi_list[-1])

    # 设置中文字体（思源宋体）
    # https://matplotlib.org/stable/api/font_manager_api.html
    # https://github.com/adobe-fonts/source-han-serif/tree/release/
    # https://github.com/adobe-fonts/source-han-serif/raw/release/OTF/SourceHanSerifSC_EL-M.zip
    font_path = "SourceHanSerifSC_EL-M/SourceHanSerifSC-Light.otf"
    prop = mfm.FontProperties(fname=font_path)

    # 函数figure()用于指定图表的宽度、高度、分辨率和背景色
    fig = plt.figure(dpi=128, figsize=(10, 6))  # (10 inches x 128 dpi) x (6 inches x 128 dpi)= 1280 x 768 pixels
    # 绘图
    plt.plot(date_list, weight_list, c='red')  # 分别传入x坐标和y坐标值列表

    # 设置标题，x和y轴标签属性
    plt.title("Harvey's Weight Records From 2021", fontsize=24)
    # 添加网格
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grid.html
    plt.grid(True)
    plt.xlabel("最佳BMI值范围: 19-24 当前值: "
               + last_bmi + " 最后更新: " + last_date, fontsize=16, fontproperties=prop)
    # https://matplotlib.org/stable/api/figure_api.html?highlight=autofmt_xdate#matplotlib.figure.Figure.autofmt_xdate
    fig.autofmt_xdate()  # 绘制斜的日期标签，默认参数值为右对齐旋转30度
    plt.ylabel("Weight (Kg)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    # plt.show()
    saved_file = datetime.datetime.now().strftime('%Y%m%d%H%M%S')  # 日期对象转换为日期字符串
    plt.savefig(saved_file + '.png')


# 提示用户输入并判断输入有效性
def menu():
    # 打印信息，提示用户操作
    print("请选择将要执行的操作:\n"
          "1) 录入新数据\n"
          "2) 查看可视化数据\n"
          "q) 退出程序")

    option = input("请输入编号并按回车键: ")
    if option == '1':
        print("开始数据录入……")
        data_input()
    elif option == '2':
        print("开始数据输出……")
        data_output()
    elif option == 'q':
        exit()
    else:
        print("输入错误")


# 程序启动默认调用menu()函数
menu()
