#coding=utf-8
# -*- coding:utf-8 -*-

print('你好')

#在python中，只要定义了一个变量，而且它有数据，那么它的类型就已经确定了，
# 不需要咱们开发者主动的去说明它的类型，系统会自动辨别
#可以使用type(变量的名字)，来查看变量的类型

num1 = 1
num2 = 2
value = num1 + num2
print(value)

age = 18
name = "Test"
qq = 469672930
phoneNum = 15626484411
site = "广州市"
print("今年%s岁\n叫%s"%(age,name))

print("==========我的名片==========\n姓名: %s\nQQ:%s\n手机号:%s\n公司地址:%s\n==========================="%(name,qq,phoneNum,site))