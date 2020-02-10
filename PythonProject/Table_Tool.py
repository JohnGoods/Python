# -*- coding: utf-8 -*-
# @Time : 2020/2/10 15:35
# @Author : jjh
# @File : Table_Tool.py
# @Software: PyCharm
# @contact: 469672930@qq.com
# -*- 功能说明 -*-
# 列表或者字典工具
# -*- 功能说明 -*-


#重复元素判定
# tool.ListUnique([1,1,2]) # True
def ListUnique(lst):
    return len(lst) == len(set(lst))

#按数量切割列表
from math import ceil
def SplitListByCount(lst, count):
    return list(
        map(lambda x: lst[x * count:x * count + count],
            list(range(0, ceil(len(lst) / count)))))

#展开列表
#该方法将通过递归的方式将列表的嵌套展开为单个列表
def Spread(arg):
    ret = []
    for i in arg:
        if isinstance(i, list):
            ret.extend(i)
        else:
            ret.append(i)
    return ret
def DeepFlatten(lst):
    result = []
    result.extend(
        Spread(list(map(lambda x: DeepFlatten(x) if type(x) == list else x, lst))))
    return result
#DeepFlatten([1, [2], [[3], 4], 5]) # [1,2,3,4,5]

#检查列表是不是有重复项。
def HasDuplicates(lst):
    return len(lst) != len(set(lst))
#HasDuplicates([1,2,3,4,5,5]) # True

#合并两个字典（覆盖更新）
def MergeTwoDicts(a, b):
    c = a.copy()   # make a copy of a
    c.update(b)    # modify keys and values of a with the ones from b
    return c
#3.5版本以上合并方法
def MergeTwoDicts2(a, b):
   return {**a, **b}
#a = { 'x': 1, 'y': 2}
#b = { 'y': 3, 'z': 4}
#print(MergeTwoDicts(a, b))
# {'y': 3, 'x': 1, 'z': 4}

#将两个列表转化为单个字典
def ToDictionary(keys, values):
    return dict(zip(keys, values))
#keys = ["a", "b", "c"]
#values = [2, 3, 4]
#print(ToDictionary(keys, values))
# {'a': 2, 'c': 4, 'b': 3}

#检查字典key是否none
def checkDictHaveKey(dict,key):
        return key in dict

#Shuffle
#该算法会打乱列表元素的顺序，它主要会通过 Fisher-Yates 算法对新列表进行排序
from copy import deepcopy
from random import randint
def Shuffle(lst):
    temp_lst = deepcopy(lst)
    m = len(temp_lst)
    while (m):
        m -= 1
        i = randint(0, m)
        temp_lst[m], temp_lst[i] = temp_lst[i], temp_lst[m]
    return temp_lst
#print(tool.Shuffle([1,2,3,4,5,6,7])) #[1, 3, 2, 7, 5, 6, 4]

#展开列表
#将列表内的所有元素，包括子列表，都展开成一个列表
def Spread(arg):
    ret = []
    for i in arg:
        if isinstance(i, list):
            ret.extend(i)
        else:
            ret.append(i)
    return ret
#tool.Spread([1,2,3,[4,5,6],[7],8,9]) # [1,2,3,4,5,6,7,8,9]

#检查两个字符串的组成元素是不是一样
# tool.Anagram("abcd3", "3acdb") # True
from collections import Counter
def Anagram(first, second):
    return Counter(first) == Counter(second)

#解压序列赋值给多个变量
def GiveMoreValue():
    data = ['ACME', 50, 91.1, (2012, 12, 21)]
    _, shares, price, _ = data
    print(shares)
    print(price)

# 解压可迭代对象赋值给多个变量
# 如果一个可迭代对象的元素个数超过变量个数时，会抛出一个 ValueError 。 那么怎样才能从这个可迭代对象中解压出 N 个元素出来？
'''
下面是一个带有标签的元组序列
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)'''
def GiveMoreValue2():
    *trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
    print(trailing)
    print(current)

    # 星号解压语法
    # line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
    # uname, *fields, homedir, sh = line.split(':')
    # print(fields)

    record = ('ACME', 50, 123.45, (12, 18, 2012))
    name, *_, (*_, year) = record
    print(name,'--',year)

# 保留匹配到的字符串最后 N 个元素
# 保留有限历史记录
# 简单的文本匹配， 并返回匹配所在行的最后N行
from collections import deque
def search(lines, pattern, history):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

def filePiPeiTextBaoLiuNum(fileText = None, str = None, Num = None):
    if fileText == None:
        fileText = r'somefile.txt'
    if str == None:
        str = 'python'
    if Num == None:
        Num = 5
    with open(fileText) as f:
        for line, prevlines in search(f, str,Num):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)

# 查找最大或最小的 N 个元素
# 怎样从一个集合中获得最大或者最小的 N 个元素列表?
import heapq
def FindMaxOrMinByCollection(collection = None, MaxCount = None, MinCount = None, isLambda = None, findKey = None):
    if collection == None:
        collection = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    if MaxCount == None:
        MaxCount = 1
    if MinCount == None:
        MinCount = 1
    if isLambda == None:
        isLambda = False
    if isLambda == True:
        if findKey == None:
            collection = [
                {'name': 'IBM', 'shares': 100, 'price': 91.1},
                {'name': 'AAPL', 'shares': 50, 'price': 543.22},
                {'name': 'FB', 'shares': 200, 'price': 21.09},
                {'name': 'HPQ', 'shares': 35, 'price': 31.75},
                {'name': 'YHOO', 'shares': 45, 'price': 16.35},
                {'name': 'ACME', 'shares': 75, 'price': 115.65}
            ]
            findKey = 'shares'
    if isLambda == True:
        xpensive = heapq.nlargest(MinCount, collection, key=lambda s: s[findKey])
        cheap = heapq.nsmallest(MaxCount, collection, key=lambda s: s[findKey])
    else:
        xpensive = heapq.nsmallest(MinCount,collection)
        cheap =  heapq.nlargest(MaxCount,collection)

    return xpensive,cheap

# 字典中的键映射多个值
# 怎样实现一个键对应多个值的字典
from collections import defaultdict
def collectionMoreKey():
    a = {'a': (1,2), 'b': '2', 'c': '3'}
    d = {}
    for key, value in a.items():
        if key not in d:
            d[key] = []
        d[key].append(value)
    print(d)
    print("==========")
    dd = defaultdict(list)
    for key, value in a.items():
        dd[key].append(value)
    print(dd)

# 字典排序
from collections import OrderedDict
import json
# OrderedDict 内部维护着一个根据键插入顺序排序的双向链表。每次当一个新的元素插入进来的时候，
# 它会被放到链表的尾部。对于一个已经存在的键的重复赋值不会改变键的顺序
def SortDictionary():
    #根据插入顺序排序
    d = OrderedDict()
    d['foo'] = "s"
    d['bar'] = "b"
    d['grok'] = "t"
    d['spam'] = "a"

    # Outputs "foo 1", "bar 2", "spam 3", "grok 4"
    for key in d:
        print(key, d[key])
    s = json.dumps(d)
    print(type(s))
    t = json.loads(s)
    print(type(t))
    print(t)

def SortDictionaryByValue(_dictionary = None):
    if _dictionary == None:
        _dictionary = {
            'ACME': 45.23,
            'AAPL': 612.78,
            'IBM': 205.55,
            'HPQ': 37.20,
            'FB': 10.75
        }
    print(_dictionary)
    _dictionary_sorted = sorted(zip(_dictionary.values(), _dictionary.keys()))
    _min = min(zip(_dictionary.values(), _dictionary.keys()))
    _max = max(zip(_dictionary.values(), _dictionary.keys()))
    valueMin = min(_dictionary.values())  # Returns 10.75
    valueMax = max(_dictionary.values())  # Returns 612.78
    strMin = min(_dictionary, key=lambda k: _dictionary[k])
    strMax = max(_dictionary, key=lambda k: _dictionary[k])
    print(_dictionary_sorted)
    print(_min)
    print(_max)
    print(valueMin)
    print(valueMax)
    print(strMin)
    print(strMax)
    return _dictionary_sorted,_min,_max













