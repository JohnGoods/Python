# -*- coding: utf-8 -*-
# @Time : 2020/2/10 15:17
# @Author : jjh
# @File : String_Tool.py
# @Software: PyCharm
# @contact: 469672930@qq.com
# -*- 功能说明 -*-
# 字符串工具
# -*- 功能说明 -*-
import tool
from tool import Table_Tool

#第一个字母大写
# tool.StrFirstBig('hello World') # Hello World
def StrFirstBig(str):
    return str.title()

#首字母小写
def StrFirstSmall(str):
    return str[:1].lower() + str[1:]

#统计某个字符出现次数
# tool.CountVowels("aaas",r'[abcs]') #4
import re
def CountVowels(str,dictionaryStr):
    #dictionaryStr = r'[aeiou]'
    return len(re.findall(dictionaryStr, str, re.IGNORECASE))

#检查是否回文序列
#以下方法会检查给定的字符串是不是回文序列，它首先会把所有字母转化为小写，并移除非英文字母符号。最后，它会对比字符串与反向字符串是否相等，相等则表示为回文序列
def Palindrome(string):
    from re import sub
    s = sub('[\W_]', '', string.lower())
    return s == s[::-1]
#print(tool.Palindrome('abc ba')) #True

#不需要额外的操作就能交换两个变量的值。
def Swap(a, b):
  return b, a
#print(tool.Swap(-1, 14)) # (14, -1))


# 使用多个界定符分割字符串
# 你需要将一个字符串分割为多个字段，但是分隔符(还有周围的空格)并不是固定的
# maxsplit = 分割次数
import re
#re.split(pattern, string, maxsplit=0, flags=0)
def Split(str, line, maxsplitCount=0,_flags=0):
    #str = r'[;,\s]\s*'
    #re.split(r'(;|,|\s)\s*', line) #这样的话---括号---里被匹配的文本也将出现在结果列表中
    #(?:..)这样不会捕捉括号的字符
    return re.split(str, line, maxsplit=maxsplitCount, flags=_flags)

#字符串开头或结尾匹配
#你需要通过指定的文本模式去检查字符串的开头或者结尾，比如文件名后缀，URL Scheme等等
import os
def FileHaveName(startStr = ('00','tool'),endStr ='.py',anyType = ('.c', '.h')):
    filenames = os.listdir('.')
    print([name for name in filenames if name.startswith(startStr)]) #打印所有开头包含00或者tool的文件
    print([name for name in filenames if name.endswith(endStr)])  # 打印所有结尾包含.py的文件
    #某个文件夹中是否存在指定的文件类型
    print(any(name.endswith(anyType) for name in filenames)) #true or false
    # 还可以下面这样匹配其中的字符
    # import re
    # url = 'http://www.python.org'
    # re.match('http:|https:|ftp:', url)

#通过文本匹配读网址
from urllib.request import urlopen
def ReadUrlData():
    urlName = tuple(["test","https://www.baidu.com/"]) #要确保传递参数前先调用 tuple() 将其转换为元组类型
    for name in urlName:
        if name.startswith(('http:', 'https:', 'ftp:')):
            return urlopen(name).read()
        else:
            print(name + "------> is not url")
            # with open(name) as f:
            #     return f.read()

#字符串匹配和搜索
import re
def GetStrByGuide(guide = re.compile(r'(\d+)/(\d+)/(\d+)'), text = '8/2/2020',groupIndex = 0):
    print(text)
    if guide.match(text):   #精确查找 xx/xx/xx
        m = guide.match(text)
        print(m.group(groupIndex))
        print(m.group(m.lastindex))
        month, day, year = m.groups()
        print('{}-{}-{}'.format(year, month, day))
        newText = "Today is 8/2/2020. Tomorrow is 9/2/2020."
        print(newText)
        listText = guide.findall(newText)
        print(listText)
        for month, day, year in guide.findall(newText):
            print('{}-{}-{}'.format(year, month, day))
    else:
        print("not find")

#字符串简单替换(简单模式)
def StrReplace(replaceText = 'yeah, but no, but yeah, but no, but yeah', needReplacestr = 'yeah' ,replaceStr = 'yep'):
    newText = replaceText.replace(needReplacestr, replaceStr)
    print(newText)

#字符串搜索和替换(复杂的模式)
import re
def StrFindAndReplace():
    month_abbr = ["a","b","c","d","f","g","h","i","j","k","l","m","n"]
    guide = re.compile(r'(\d+)/(\d+)/(\d+)')
    m = guide.match('8/2/2020')
    monthName = month_abbr[int(m.group(2))]
    print(monthName)

    text = 'Today is 2/8/2020. Tomorrow is 2/9/2020.'
    newText = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3年\1月\2日', text)
    text,n = re.subn(r'(\d+)/(\d+)/(\d+)', r'\3年\1{month}\2日'.format(month=monthName), text) #subn 可以知道替换次数
    print("替换次数:"+str(n))
    print(newText)
    print(text)

#字符串忽略大小写的搜索替换
# 忽略大小写的
def StrReplace():
    text = 'UPPER PYTHON, lower python, Mixed Python'
    re.findall('python', text, flags=re.IGNORECASE)
    newText = re.sub('python', Matchcase('snake'), text, flags=re.IGNORECASE)
    print(newText)
#(辅助函数)
def Matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace

#最短匹配模式
def ZuiDuanPiPei():
    text = 'Computer says "no." Phone says "yes."'
    str_pat = re.compile(r'"(.*?)"')
    print(str_pat.findall(text))

#多行匹配模式
def MorePiPet():
    text = '''/* this is a
    ... multiline comment */
    ... '''
    comment = re.compile(r'/\*((?:.|\n)*?)\*/')
    #comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)  #这样也可以
    print(comment.findall(text))

#将Unicode文本标准化
import unicodedata
def UnicodeChange(str = 'Spicy Jalape\u00f1o',isCleanYuanYin = True,isUpper = True):
    # s1 = 'Spicy Jalape\u00f1o'
    # s2 = 'Spicy Jalapen\u0303o'
    # print(s1 == s2)
    # t1 = unicodedata.normalize('NFC', s1)
    # t2 = unicodedata.normalize('NFC', s2)
    # print(t1 == t2)
    # t3 = unicodedata.normalize('NFD', s1)
    # print(ascii(t1))
    # print(ascii(t3))
    #
    # print(s1)
    # n1 = unicodedata.normalize('NFD', s1)
    # print(''.join(c for c in n1 if not unicodedata.combining(c)))   #除掉一些文本上面的变音符
    returnText = unicodedata.normalize('NFC', str)
    if isCleanYuanYin :
        returnText = unicodedata.normalize('NFD', str)
        returnText = ''.join(c for c in returnText if not unicodedata.combining(c))
    if isUpper :
        returnText = returnText.upper()
    return returnText

#删除字符串中不需要的字符
''' #规则
    # 匹配任意1个字符（除了\n）
    # []
    # 匹配[]中列举的字符
    # \d
    # 匹配数字，即0 - 9
    # \D
    # 匹配非数字，即不是数字
    # \s
    # 匹配空白，即 空格，tab键
    # \S
    # 匹配非空白
    # \w
    # 匹配非特殊字符，即a - z、A - Z、0 - 9、_、汉字
    # \W
    # 匹配特殊字符，即非字母、非数字、非汉字、非_
    */
'''
def DelectStrAnyChar(str =  'hello     world \n', delectStr = ' '):
    #str.strip()  #方法能用于删除开始或结尾的字符
    # t = '-----hello World====='
    # print(t.lstrip('-')) #lstrip() 从左执行删除操作 #hello World=====
    # print(t.rstrip('=')) #rstrip() 从右执行删除操作 #-----hello World
    # print(t.strip('-=')) #strip() 删除指定字符 #hello World

    # newStr =  str.replace(delectStr, '')
    # print(newStr)
    # guide = str.replace(delectStr, '') #空白删除
    # re.sub('l|h', '', guide) #多个不一样的字符删除 或者替换
    return re.sub(delectStr, '', str)
    # 通常情况下你想将字符串 strip 操作和其他迭代操作相结合，比如从文件中读取多行数据。
    # 如果是这样的话，那么生成器表达式就可以大显身手了。比如
    # with open(filename) as f:
        # lines = (line.strip() for line in f)
        # for line in lines:
        #     print(line)

# 审查清理文本字符串
# 一些无聊的幼稚黑客在你的网站页面表单中输入文本”pýtĥöñ”，然后你想将这些字符清理掉
# 或者是某些广告词
# str.translate()
import unicodedata
import sys
# 以后有空把这些字符写个函数让它开始加载,或者保存在表单
def CleanRubbishStr(needCleanStr = 'pýtĥöñ\fis\tawesome\r\n'):
    remap = {
        ord('\t'): ' ',
        ord('\f'): ' ',
        ord('\n'): None,  # Deleted
        ord('\r'): None,  # Deleted
    }
    print("remap Count is " + str(len(remap)))

    remap2 = dict.fromkeys(c for c in range(sys.maxunicode)
            if unicodedata.combining(chr(c)))
    print("remap2 Count is " + str(len(remap2)))
    # a = needCleanStr.translate(remap)
    # print(a)
    # b = unicodedata.normalize('NFD', a)
    # print(b)
    # b = b.translate(remap2)
    # print(b)

    digitmap = {
        c: ord('0') + unicodedata.digit(chr(c))
        for c in range(sys.maxunicode)
             if unicodedata.category(chr(c)) == 'Nd'
    }
    print("digitmap Count is " + str(len(digitmap)))
    # x = '\u0661\u0662\u0663'
    # print(x.translate(digitmap))

    allList = tool.MergeTwoDicts(remap,remap2)
    allList = tool.MergeTwoDicts(allList, digitmap)
    print("allList Count is " + str(len(allList)))

    a = unicodedata.normalize('NFD', needCleanStr)
    b = a.translate(allList)
    print(b)

# 字符串对齐
# 你想通过某种对齐方式来格式化字符串
def StrAlignment(text = 'Hello World', alignment = 'left',aligStr = ' ',distance = 20):
    action = {
        "left": text.ljust,
        "right": text.rjust,
        "center": text.center
    }

    if not Table_Tool.checkDictHaveKey(action,alignment):
        return "alignment " + alignment + " is none"
    else:
        return action[alignment](distance,aligStr)

#字符串对齐(format)方式
def StrAlignmentFormat(text = 'Hello World', alignment = 's',aligStr = ' ',distance = 20):
    action = {
        "left": '<',
        "right": '>',
        "center": '^'
    }
    if not Table_Tool.checkDictHaveKey(action,alignment):
        #一个相对比较聪明的技巧是利用生成器表达式(参考1.19小节)转换数据为字符串的同时合并字符串，比如：
        data = 'alignment ',alignment,' is none'
        #print('alignment ', alignment, ' is none', sep=' ') #better
        return ' '.join(str(d) for d in data)
    else:
        aligementStr = action[alignment]
        #print('{:<10s} {:>10s}'.format('Hello', 'World'))
        return format(text, aligStr + aligementStr + str(distance))
    #More
    #'{:<10s} {:>10s}'.format('Hello', 'World')

# 防止key找不到
class Safesub(dict):
    def __missing__(self, key):
        return '{' + key + '}'

# 字符串中插入变量
# 你想创建一个内嵌变量的字符串，变量被它的值所表示的字符串替换掉
def strInsertValue():
    text = '{name} has {n} messages.'
    name = 'Guido'
    n = 37
    # text.format(name='Guido', n=37)
    print(text.format_map(vars()))
    #高级用法
    class Info:
        def __init__(self, name, n,t="{t"):
            self.name = name
            self.n = n

    a = Info('Guido', 37)
    text = '{name} has {n} messages{tt}.'
    #print(text.format_map(vars(a))) #报错
    #print(text.format(name='Guido'))    #错误例子，因为不能很好的处理变量缺失的情况 n=?
    #del a.n
    print(text.format_map(Safesub(vars(a)))) #做了安全保护

# here
def StringFarmatByDirt(cns=None,dirtList = None):
    if dirtList == None:
        dirtList = {'name': '小明', 'class': '20190301', 'score': 597.5}
    if cns == None:
        cns = '{class}班-{name}总分：{%t}'
    print(cns.format_map(Safesub(dirtList)))

def StringFarmatByList(cns=None, strList=None):
    if strList is None:
        strList = ['a', 'b', 'c']
    if cns is None:
        cns = '{t0} has {t1} messages{t3}.'

    class Info:
        def __init__(self, strList=None):
            keyListInfo = {}
            for index, value in enumerate(strList):
                key = 't{}'.format(index)
                keyListInfo[key] = value
            #还得判断字典是否有值...
            self.t0 = keyListInfo["t0"]
            self.t1 = keyListInfo["t1"]
            self.t2 = keyListInfo["t2"]

    info = Info(strList)
    print(cns.format_map(Safesub(vars(info))))

# 以指定列宽格式化字符串
# 你有一些长字符串，想以指定的列宽将它们重新格式化
import textwrap
import os
def StrFormat(str = '',formatNum = 60, titleIndent=True, subIndent = False, isTerminalModel = False):
    str = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."
    if isTerminalModel == True:
        size = os.get_terminal_size()
        # columns = size.columns
        # lines = size.lines
        formatNum = size.columns
    titleStr = ''
    subStr = ''
    if titleIndent == True:
        titleStr = '    '
    if subIndent == True:
        subStr = '    '
    print(textwrap.fill(str, formatNum, initial_indent=titleStr, subsequent_indent=subStr))

# 在字符串中处理html和xml
# 你想将HTML或者XML实体如 &entity; 或 &#code; 替换为对应的文本。 再者，你需要转换文本中特定的字符(比如<, >, 或 &)
import html
from html.parser import HTMLParser #a
#from xml.sax.saxutils import unescape #b
def StrHandleHtmlAndXml(handleMlStr = 'Elements are written as "<tag>text</tag>".',xmlStr = 'Elements are written as "&lt;tag&gt;text&lt;/tag&gt;".'):
    #解释
    print(handleMlStr)
    print(html.escape(handleMlStr))
    print(html.escape(handleMlStr, quote=False))

    #还原
    a = xmlStr
    b = xmlStr
    from html.parser import HTMLParser
    p = HTMLParser()
    x = p.unescape(a)
    print(x)
    from xml.sax.saxutils import unescape
    y = unescape(b)
    print(y)

    s = 'Spicy Jalapeño'
    print(s.encode('ascii', errors='xmlcharrefreplace'))

# 字符串令牌解析
# 你有一个字符串，想从左至右将其解析为一个令牌流
import re
from collections import Counter, namedtuple
def TokenStr():
    text = 'foo = 23 + 42 * 10'
    # text = 'foo = 23 + 42'
    NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
    NUM = r'(?P<NUM>\d+)'
    PLUS = r'(?P<PLUS>\+)'
    TIMES = r'(?P<TIMES>\*)'
    EQ = r'(?P<EQ>=)'
    WS = r'(?P<WS>\s+)'
    master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))

    def generate_tokens(pat, text):
        Token = namedtuple('Token', ['type', 'value'])
        scanner = pat.scanner(text)
        for m in iter(scanner.match, None):
            yield Token(m.lastgroup, m.group())


    # Example use
    # for tok in generate_tokens(master_pat, text ):
    #     print(tok)

    # print("-")
    tokens = (tok for tok in generate_tokens(master_pat, text)
              if tok.type != 'WS')
    for tok in tokens:
        print(tok)

    print("============")
    PRINT = r'(?P<PRINT>print)'
    NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'

    master_pat = re.compile('|'.join([PRINT, NAME]))
    for tok in generate_tokens(master_pat, 'printer'):
        print(tok)