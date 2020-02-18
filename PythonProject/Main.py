# -*- coding: utf-8 -*-
# @Time : 2020/2/6 18:28
# @Author : jjh
# @File : 000_Test.py
# @Software: PyCharm
# @contact: 469672930@qq.com
# -*- 功能说明 -*-
# 测试用
# -*- 功能说明 -*-
from logic.ConfigPathSys import ConfigPathSystem
from tool.Filter import DFAFilter
from tool import Tool,String_Tool,Table_Tool,Math_Tool,Time_Tool,Iter_Tool,Filter

Model = 2
def InitFuc():
    Tool.SetPrintDisable(True)
    ConfigPathSystem()  # 直接初始化
    DFAFilter()  # 直接初始化

def Start():
    print("main.fuc")

def Test():
    value = Tool.NeedTime(Iter_Tool.SmallIter())
    if not value == None:
        print(value)

if __name__ == "__main__":
    Tool.NeedTime(InitFuc)
    #self: InitFuc()
    if Model == 1:
        self:Start()
    elif Model == 2:
        self:Test()
