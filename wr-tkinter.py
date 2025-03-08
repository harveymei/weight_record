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
7，引入tkinter模块，实现GUI界面
"""

# 导入Python内置模块和外部模块
import os
import csv
import datetime
from matplotlib import pyplot as plt
import matplotlib.font_manager as mfm
import tkinter as tk
from tkinter import messagebox, simpledialog

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
    current_date = simpledialog.askstring("输入日期", f"请输入当前日期数值或直接按回车键使用默认数值: ({system_date}) ", parent=root)
    if current_date == '':
        current_date = system_date

    current_height = simpledialog.askstring("输入身高", f"请输入当前身高数值或直接按回车键使用默认数值(m): (1.72) ", parent=root)
    if current_height == '':
        current_height = 1.72

    current_weight = simpledialog.askstring("输入体重", "请输入当前体重数值(kg): ", parent=root)

    current_bmi = round(float(current_weight) / (float(current_height) ** 2), 2)

    # 拼接数据
    new_data = current_date + ',' + str(current_height) + ',' + current_weight + ',' + str(current_bmi) + '\n'

    # 写入文件，追加写模式
    with open(filename, 'a') as f_object:
        f_object.write(new_data)

    messagebox.showinfo("录入完成", "录入完成.")
    if messagebox.askyesno("继续操作", "按是继续或按否退出. ", parent=root):
        data_input()
    else:
        menu()

def data_output():
    """
    数据输出函数
    """
    with open(filename) as f_object:
        reader = csv.reader(f_object)
        header_row = next(reader)  # 读取文件头（首行）

        date_list, weight_list, bmi_list = [], [], []  # 定义空列表以存储遍历到的数据
        for row in reader:  # 从第二行开始遍历
            date = datetime.datetime.strptime(row[0], '%Y-%m-%d')  # 字符串日期转换为日期对象
            weight = float(row[2])  # 将遍历到的字符串数值转换为浮点数
            bmi = float(row[-1])

            date_list.append(date)
            weight_list.append(weight)
            bmi_list.append(bmi)
            last_date = datetime.datetime.strftime(date_list[-1], '%Y-%m-%d')
            last_bmi = str(bmi_list[-1])

    # 设置中文字体（思源宋体）
    font_path = "SourceHanSerifSC_EL-M/SourceHanSerifSC-Light.otf"
    prop = mfm.FontProperties(fname=font_path)

    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(date_list, weight_list, c='red')

    plt.title("Harvey's Weight Records From 2021", fontsize=24)
    plt.grid(True)
    plt.xlabel("最佳BMI值范围: 19-24 当前值: "
               + last_bmi + " 最后更新: " + last_date, fontsize=16, fontproperties=prop)
    fig.autofmt_xdate()
    plt.ylabel("Weight (Kg)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    saved_file = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    plt.savefig(saved_file + '.png')
    messagebox.showinfo("保存完成", f"图表已保存为 {saved_file}.png")

def menu():
    root.geometry("300x150")
    root.title("体重记录系统")

    label = tk.Label(root, text="请选择将要执行的操作:", font=('Arial', 12))
    label.pack(pady=10)

    button_input = tk.Button(root, text="录入新数据", command=data_input)
    button_input.pack(pady=5)

    button_output = tk.Button(root, text="查看可视化数据", command=data_output)
    button_output.pack(pady=5)

    button_exit = tk.Button(root, text="退出程序", command=root.quit)
    button_exit.pack(pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    menu()
    root.mainloop()
