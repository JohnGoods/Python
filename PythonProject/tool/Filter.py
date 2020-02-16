# -*- coding: utf-8 -*-
# @Time : 2020/2/10 15:07
# @Author : jjh
# @File : InterpreterTool.py
# @Software: PyCharm
# @contact: 469672930@qq.com
# -*- 功能说明 -*-
#  过滤器
# -*- 功能说明 -*-

# -*- coding:utf-8 -*-
import os
# from logic import configPath
# DFA算法
import threading
from logic.ConfigPathSys import ConfigPathSystem

class DFAFilter(object):
    initFlag = False

    def __init__(self):
        if self.initFlag == True:
            pass
        else:
            self._init()

    _instance_lock = threading.Lock()
    def __new__(cls, *args, **kwargs):
        if not hasattr(DFAFilter, "_instance"):
            with DFAFilter._instance_lock:
                if not hasattr(DFAFilter, "_instance"):
                    DFAFilter._instance = object.__new__(cls)
        return DFAFilter._instance

    def _init(self):
        self.keyword_chains = {}  # 关键词链表
        self.delimit = '\x00'  # 限定
        path = ConfigPathSystem().keywordsPath #过滤表路径
        # path = ConfigPathSystem().getPathByName("keywords")
        with open(path, encoding='utf-8') as f:
            for keyword in f:
                self.add(str(keyword).strip())
        #print(self.keyword_chains)
        self.initFlag = True

    # 添加过滤词
    def add(self, keyword):
        keyword = keyword.lower()  # 关键词英文变为小写
        chars = keyword.strip()  # 关键字去除首尾空格和换行
        if not chars:  # 如果关键词为空直接返回
            return
        level = self.keyword_chains
        # 遍历关键字的每个字
        for i in range(len(chars)):
            # 如果这个字已经存在字符链的key中就进入其子字典
            if chars[i] in level:
                level = level[chars[i]]
            else:
                if not isinstance(level, dict):
                    break
                for j in range(i, len(chars)):
                    level[chars[j]] = {}
                    last_level, last_char = level, chars[j]
                    level = level[chars[j]]
                last_level[last_char] = {self.delimit: 0}
                break
        if i == len(chars) - 1:
            level[self.delimit] = 0

    # 检查是否有敏感词
    def checkSensitiveWords(self,text):
        message = text.lower()
        ret = []
        start = 0
        while start < len(message):
            level = self.keyword_chains
            step_ins = 0
            for char in message[start:]:
                if char in level:
                    step_ins += 1
                    if self.delimit not in level[char]:
                        level = level[char]
                    else:
                        return True
                else:
                    break
            start += 1
        return False

    #过滤敏感词
    def filter(self, message, repl="*"):
        message = message.lower()
        ret = []
        start = 0
        while start < len(message):
            level = self.keyword_chains
            step_ins = 0
            for char in message[start:]:
                if char in level:
                    step_ins += 1
                    if self.delimit not in level[char]:
                        level = level[char]
                    else:
                        ret.append(repl * step_ins)
                        start += step_ins - 1
                        break
                else:
                    ret.append(message[start])
                    break
            else:
                ret.append(message[start])
            start += 1
        return ''.join(ret)

# text = "习近平"
# print(DFAFilter().checkSensitiveWords(text))
# print(DFAFilter().filter(text))