# 字符 	功能
# * 	匹配前一个字符出现0次或者无限次，即可有可无
# + 	匹配前一个字符出现1次或者无限次，即至少有1次
# ? 	匹配前一个字符出现1次或者0次，即要么有1次，要么没有
# {m} 	匹配前一个字符出现m次
# {m,n} 	匹配前一个字符出现从m到n次


# 匹配分组
# 字符 	功能
# | 	匹配左右任意一个表达式
# (ab) 	将括号中字符作为一个分组
# \num 	引用分组num匹配到的字符串
# (?P<name>) 	分组起别名
# (?P=name) 	引用别名为name分组匹配到的字符串
#coding=utf-8

import re
# 需求：匹配出0-100之间的数字
ret = re.match("[1-9]?\d$|101","101")
if ret:
    print(ret.group())
else:
    print("不在0-101之间")

#不是以4、7结尾的手机号码(11位)
tels = ["13100001234", "18912344321", "10086", "18800007777"]
for tel in tels:
    ret = re.match("1\d{9}[4 || 7]", tel)
    if ret:
        print(ret.group())
    else:
        print("%s 不是想要的手机号" % tel)

# 提取区号和电话号码
ret = re.match("(\d+)--(\d+)","010--12345678")
print(ret.group(1))
print(ret.group(2))