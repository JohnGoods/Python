# -*- coding: utf-8 -*-
# @Time : 2020/2/6 18:28
# @Author : jjh
# @File : 000_Test.py
# @Software: PyCharm
# @contact: 469672930@qq.com
# -*- 功能说明 -*-
# 测试用
# -*- 功能说明 -*-

import tool
import String_Tool
import Table_Tool
import Table_Tool
import Math_Tool

def InitFuc():
    tool.SetPrintDisable(True)


if __name__ == "__main__":
    self: InitFuc()
    value = Math_Tool.MathPHR()
    if not value == None:
        print(value)
