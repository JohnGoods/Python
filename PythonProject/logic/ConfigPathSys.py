# -*- coding: utf-8 -*-
# @Time : 2020/2/10 15:07
# @Author : jjh
# @File : InterpreterTool.py
# @Software: PyCharm
# @contact: 469672930@qq.com
# -*- 功能说明 -*-
#  保存config路径文本
# -*- 功能说明 -*-

import os
import threading

class ConfigPathSystem(object):
    initFlag = False
    keywordsPath = ""  #敏感字库路径

    def __init__(self):
        if self.initFlag == True:
            pass
        else:
            self.initPath()

    _instance_lock = threading.Lock()
    def __new__(cls, *args, **kwargs):
        if not hasattr(ConfigPathSystem, "_instance"):
            with ConfigPathSystem._instance_lock:
                if not hasattr(ConfigPathSystem, "_instance"):
                    ConfigPathSystem._instance = object.__new__(cls)
        return ConfigPathSystem._instance

    def initPath(self):
        curPath = os.getcwd()
        # lastDir = os.path.dirname(curPath)
        self.keywordsPath = curPath + "\\config\\keywords.txt"
        self.initFlag = True
