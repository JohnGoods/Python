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

from tool import Tool
from tool import String_Tool
from tool import Table_Tool
from tool import Math_Tool
from tool import Time_Tool
from tool import Filter

def InitFuc():
    Tool.SetPrintDisable(True)
    # ConfigPathSys.InitConfigPath()
    ConfigPathSystem() #直接初始化
    DFAFilter() #直接初始化

if __name__ == "__main__":
    self:InitFuc()
    text = "习近平"
    print(DFAFilter().checkSensitiveWords(text))
    print(DFAFilter().filter(text))
    # value = Math_Tool.MathMatrix()
    # if not value == None:
    #     print(value)
