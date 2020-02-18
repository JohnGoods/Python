# -*- coding: utf-8 -*-
# @Time : 2020/2/18 20:22
# @Author : jjh
# @File : Iter_Tool.py
# @Software: PyCharm
# @contact: 469672930@qq.com
# -*- 功能说明 -*-
# 迭代器工具
# -*- 功能说明 -*-
import os

# 简单的迭代器
def SmallIter():
    fileText = u'{}\\tool\\somefile.txt'.format(os.getcwd())
    with open(fileText) as f:
        while True:
            line = next(f, None)
            if line is None:
                break
            print(line, end='')
    print("\n=========")
    items = [1, 2, 3]
    it = iter(items)
    print(next(it))
    print(next(it))
    print(next(it))
    try:
        print(next(it))
    except StopIteration: #StopIteration 用来指示迭代的结尾
        print("error StopIteration")