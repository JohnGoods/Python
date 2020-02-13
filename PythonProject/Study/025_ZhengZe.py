#coding=utf-8

# 导入re模块
import re

# 使用match方法进行匹配操作
#result = re.match(正则表达式, 要匹配的字符串)

# 字符 	功能
# . 	匹配任意1个字符（除了\n）
# [ ] 	匹配[ ]中列举的字符
# \d 	匹配数字，即0-9
# \D 	匹配非数字，即不是数字
# \s 	匹配空白，即 空格，tab键
# \S 	匹配非空白
# \w 	匹配单词字符，即a-z、A-Z、0-9、_
# \W 	匹配非单词字符

# 如果上一步匹配到数据的话，可以使用group方法来提取数据
# result = re.match("itcast","itcast.cn")
# print(result.group())

# ret = re.match(".","M")
# print(ret.group())
#
# ret = re.match("t.o","too")
# print(ret.group())

# str = str(input("输入密码"))
# ret = re.match("[a-zA-Z0-9_]{8,20}@\.com$",str)
email_list = ["xiaoWang@163.com", "xiaoWang@163.comheihei", ".com.xiaowang@qq.com"]
for email in email_list:
    ret = re.match("[a-zA-Z0-9_]{8,20}@163\.com$",email)
    #ret = re.match("[\w]{4,20}@163\.com$", email)
    if ret :
        print(ret.group())
    else:
        print("not")
