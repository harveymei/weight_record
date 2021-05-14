#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/5/14 5:05 下午
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: weight_record.py
# @IDE     : PyCharm
# @GitHub  : https://github.com/harveymei/

# Python Cook Book 参考目录
# Json操作 6.2
# 文件操作 5.5

# 检测文件是否存在
import os

# 检查文件是否存在，不存在则创建
if not os.path.exists('weight_record.json'):
    with open('weight_record.json', 'wt') as f:
        f.write('[]')

print("hello world!")

# 打印信息，提示用户操作
print("Choose your option:\n"
      "1) Input new weight record.\n"
      "2) View record data.")

# 提示用户输入并判断输入有效性
choice = input("you number: ")
if choice == '1':
    print("you choose 1")
elif choice == '2':
    print("you 2")
else:
    print("Error")


# 定义用户录入函数
def user_input():
    date = input("input the date yyyymmdd")  # 调用系统时间自动生成
    weight = input("input the weight: ")
    if int(weight) == True  # 判断输入是否为整数或浮点数
        print("OK")
        # 判断有效范围，大于0，小于100，单位kg
    else:
        print("not int or float")

