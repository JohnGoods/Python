# search
#
# 需求：匹配出文章阅读的次数

#coding=utf-8
import re
ret = re.search(r"\d+", "阅读次数为 9999")
print(ret.group())

# findall
#
# 需求：统计出python、c、c++相应文章阅读的次数
ret = re.findall(r"[\w|\W]+ = \d+", "python = 9999, c = 7890, c++ = 12345")
print(ret)

# split 根据匹配进行切割字符串，并返回一个列表
#
# 需求：切割字符串“info:xiaoZhang 33 shandong”
ret = re.split(r":| ","info:xiaoZhang 33 shandong")
print(ret)

#请提取url地址
str = '''
<img data-original="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" src="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" style="display: inline;">
'''
ret = re.search(r"https://.*?\.jpg",str)
print(ret.group())