# -*- coding: utf-8 -*-
# @Time : 2020/2/6 18:27
# @Author : jjh
# @File : tool.py
# @Software: PyCharm
# @contact: 469672930@qq.com
# -*- 功能说明 -*-
# 工具常用函数
# 别的py引入 import tool
# -*- 功能说明 -*-

from tool import String_Tool
from tool import Table_Tool

#多次打印
# tool.PrintMore("test",2)
def PrintMore(str,count):
    #return print(str * count); #这个没换行的
    for i in range(count):
        print(str)

#字节占用
# tool.ByteSize('Hello World') # 11
def ByteSize(string):
    return(len(string.encode('utf-8')))



#将布尔型的值去掉，例如（False，None，0，“”），它使用 filter() 函数
# Compact([0, 1, False, 2, '', 3, 'a', 's', 34])
# [ 1, 2, 3, 'a', 's', 34 ]
def Compact(lst):
    return list(filter(bool, lst))

#打印Str式的list(日后要转成Str)
# tool.PrintList(["a","b","c"]) # a b c
def PrintList(lst):
    print("List data:\n" + "\n".join(lst))

#列表的差
#该方法将返回第一个列表的元素，其不在第二个列表内。如果同时要反馈第二个列表独有的元素，还需要加一句 set_b.difference(set_a)。
def Difference(a, b):
    set_a = set(a)
    set_b = set(b)
    comparison = set_a.difference(set_b)
    return list(comparison)
#Difference([1,2,3], [1,2,4]) # [3]

#链式函数调用
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
#a, b = 4, 5
#print((subtract if a > b else add)(a, b)) # 9

#使用枚举
def ListShowIndex(list):
    for index, element in enumerate(list):
        print("Value", element, "Index ", index, )
#ListShowIndex(["a", "b", "c", "d"])
# ('Value', 'a', 'Index ', 0)
# ('Value', 'b', 'Index ', 1)
# ('Value', 'c', 'Index ', 2)
# ('Value', 'd', 'Index ', 3)

#执行时间
import time
def NeedTime(func = None):
    start_time = time.time()
    #print("startTime----->",start_time)
    value = None
    if not func is None:
        value = func()
    end_time = time.time()
    total_time = end_time - start_time
    #print("endTime----->", end_time)
    if not func is None:
        print(func.__name__,"totalTime----->", total_time)
    if not value is None:
        return value

#def test():
#     a = 1
#     b = 2
#     c = a + b
#     tool.PrintMore(c,999)  # 3
# tool.NeedTime(test)

#元素频率
#下面的方法会根据元素频率取列表中最常见的元素
def MostFrequent(list):
    return max(set(list), key = list.count)
# print(tool.MostFrequent([1,2,1,2,3,2,1,4,2])) #2

#不使用 if-else 的计算子
import operator
def Operator(str, a, b):
    action = {
        "+": operator.add,
        "-": operator.sub,
        "/": operator.truediv,
        "*": operator.mul,
        "**": pow
    }
    #判断字典是否有key
    if not Table_Tool.checkDictHaveKey(action, str):
        return "str-" + str + "-is None"
    return action[str](a,b)
#print(tool.Operator('-', 50, 25))  # 25

# 禁止打印
DEBUG = False
import os, sys
def SetPrintDisable(debug = None):
    if debug == None:
        debug = DEBUG
    if debug == False:
        sys.stdout = open(os.devnull, 'w')










