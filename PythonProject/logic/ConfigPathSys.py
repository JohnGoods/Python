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
import re
import pytz

class ConfigPathSystem(object):
    initFlag = False
    keywordsPath = ""  #敏感字库路径
    countryPath = "" #国家全部路径
    countryTimeConfig = {} #国家时区配置
    countryNameConfig = {} #国家名字
    pathDict = {}

    def __init__(self):
        if self.initFlag == True:
            pass
        else:
            self.initPath()
            self.handleCountryData()

    _instance_lock = threading.Lock()
    def __new__(cls, *args, **kwargs):
        if not hasattr(ConfigPathSystem, "_instance"):
            with ConfigPathSystem._instance_lock:
                if not hasattr(ConfigPathSystem, "_instance"):
                    ConfigPathSystem._instance = object.__new__(cls)
        return ConfigPathSystem._instance

    #初始化配置文件路径
    def initPath(self):
        curPath = os.getcwd() + "\\config\\"
        # lastDir = os.path.dirname(curPath)
        self.keywordsPath = curPath + "keywords.txt"
        self.pathDict["keywords"] = self.keywordsPath
        self.pathDict["country"] = curPath + "country.txt"
        self.initFlag = True

    def handleCountryData(self):
        path = self.getPathByName("country")
        countryDirt = {}
        countryNameDirt = {}
        with open(path, encoding='utf-8') as f:
            for keyword in f:
                text = str(keyword).strip()
                keywordStr = re.split(r'[,]\s*', text)  #分离文本
                if len(keywordStr[2]) == 0:
                    continue
                try:
                    pytz.country_timezones[str(keywordStr[2])]
                except BaseException as e:
                    _str = str(e) + "==========is error Key=========="
                    print('\033[1;31m'+_str+'\033[0m')
                else:
                    #获取国家的时区代码
                    value = pytz.country_timezones[str(keywordStr[2])]
                    countryDirt[keywordStr[2]] = value
                    # if keywordStr[2] == "US":
                    #     print(value)
                    countryNameDirt[keywordStr[2]] = keywordStr[1]
                    for _ in value:
                        countryNameDirt[_] = _
        self.countryTimeConfig = countryDirt
        self.countryNameConfig = countryNameDirt

    def getCoutryData(self):
        return self.countryTimeConfig

    def getCoutryNameData(self):
        return self.countryNameConfig

    def getPathByName(self,name):
        return self.pathDict[name]