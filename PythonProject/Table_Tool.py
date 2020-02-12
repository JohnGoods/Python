# -*- coding: utf-8 -*-
# @Time : 2020/2/10 15:35
# @Author : jjh
# @File : Table_Tool.py
# @Software: PyCharm
# @contact: 469672930@qq.com
# -*- 功能说明 -*-
# 列表或者字典工具
# -*- 功能说明 -*-


# 重复元素判定
# tool.ListUnique([1,1,2]) # True
def ListUnique(lst):
    return len(lst) == len(set(lst))


# 按数量切割列表
from math import ceil


def SplitListByCount(lst, count):
    return list(
        map(lambda x: lst[x * count:x * count + count],
            list(range(0, ceil(len(lst) / count)))))


# 展开列表
# 该方法将通过递归的方式将列表的嵌套展开为单个列表
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


# DeepFlatten([1, [2], [[3], 4], 5]) # [1,2,3,4,5]

# 检查列表是不是有重复项。
def HasDuplicates(lst):
    return len(lst) != len(set(lst))


# HasDuplicates([1,2,3,4,5,5]) # True

# 合并两个字典（覆盖更新）
def MergeTwoDicts(a, b):
    c = a.copy()  # make a copy of a
    c.update(b)  # modify keys and values of a with the ones from b
    return c


# 3.5版本以上合并方法
def MergeTwoDicts2(a, b):
    return {**a, **b}


# a = { 'x': 1, 'y': 2}
# b = { 'y': 3, 'z': 4}
# print(MergeTwoDicts(a, b))
# {'y': 3, 'x': 1, 'z': 4}

# 将两个列表转化为单个字典
def ToDictionary(keys, values):
    return dict(zip(keys, values))


# keys = ["a", "b", "c"]
# values = [2, 3, 4]
# print(ToDictionary(keys, values))
# {'a': 2, 'c': 4, 'b': 3}

# 检查字典key是否none
def checkDictHaveKey(dict, key):
    return key in dict


# Shuffle
# 该算法会打乱列表元素的顺序，它主要会通过 Fisher-Yates 算法对新列表进行排序
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


# print(tool.Shuffle([1,2,3,4,5,6,7])) #[1, 3, 2, 7, 5, 6, 4]

# 展开列表
# 将列表内的所有元素，包括子列表，都展开成一个列表
def Spread(arg):
    ret = []
    for i in arg:
        if isinstance(i, list):
            ret.extend(i)
        else:
            ret.append(i)
    return ret


# tool.Spread([1,2,3,[4,5,6],[7],8,9]) # [1,2,3,4,5,6,7,8,9]

# 检查两个字符串的组成元素是不是一样
# tool.Anagram("abcd3", "3acdb") # True
from collections import Counter


def Anagram(first, second):
    return Counter(first) == Counter(second)


# 解压序列赋值给多个变量
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
    print(name, '--', year)


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


def filePiPeiTextBaoLiuNum(fileText=None, str=None, Num=None):
    if fileText == None:
        fileText = r'somefile.txt'
    if str == None:
        str = 'python'
    if Num == None:
        Num = 5
    with open(fileText) as f:
        for line, prevlines in search(f, str, Num):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)


# 查找最大或最小的 N 个元素
# 怎样从一个集合中获得最大或者最小的 N 个元素列表?
import heapq


def FindMaxOrMinByCollection(collection=None, MaxCount=None, MinCount=None, isLambda=None, findKey=None):
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
        xpensive = heapq.nsmallest(MinCount, collection)
        cheap = heapq.nlargest(MaxCount, collection)

    return xpensive, cheap


# 字典中的键映射多个值
# 怎样实现一个键对应多个值的字典
from collections import defaultdict
def collectionMoreKey():
    a = {'a': (1, 2), 'b': '2', 'c': '3'}
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
    # 根据插入顺序排序
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


# 字典的运算(排序)
# 怎样在数据字典中执行一些计算操作（比如求最小值、最大值、排序等等）
def SortDictionaryByValue(_dictionary=None):
    if _dictionary is None:
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
    return _dictionary_sorted, _min, _max


# 查找两字典的相同点
def checkDictionaryIdentical(dirt1=None, dirt2=None):
    if dirt1 is None:
        dirt1 = {
            'x': 1,
            'y': 2,
            'z': 3
        }
    if dirt2 is None:
        dirt2 = {
            'w': 10,
            'x': 11,
            'y': 2
        }
    print(dirt1.keys() & dirt2.keys())
    print(dirt1.keys() - dirt2.keys())
    print(dirt1.items() & dirt2.items())
    print("===================")
    c = dirtRemoveByKey(dirt1, {'z', 'x'})
    print(c)


# 移除字典指定的key内容
def dirtRemoveByKey(dirt=None, keyList=None):
    if dirt is None:
        return {}
    else:
        if keyList is None:
            keyList = {'z', 'x'}
        return {key: dirt[key] for key in dirt.keys() - keyList}


# 删除序列相同元素并保持顺序
# 怎样在一个序列上面保持元素顺序的同时消除重复的值
# a = [1, 5, 2, 1, 9, 1, 5, 10]
# list(Dedupe(a)) #[1, 5, 2, 9, 10]
# 这个方法仅仅在序列中元素为 hashable 的时候才管用

# a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
# list(Dedupe(a, key=lambda d: (d['x'],d['y']))) #[{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 4}]

# list(Dedupe(a, key=lambda d: d['x']))
# [{'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
def Dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


# 命名切片
# 如果你的程序包含了大量无法直视的硬编码切片，并且你想清理一下代码
def Slice(record = None,startIndex = None, stopIndex = None, stepIndex = None):
    if record is None:
        record = '....................100 .......513.25 ..........'
    SHARES = slice(20, 23)
    PRICE = slice(31, 37)
    cost = int(record[SHARES]) * float(record[PRICE])
    print(cost)
    a = slice(5, 50, 2)
    print(a.start)
    print(a.stop)
    print(a.step)   #跨步

    s = 'HelloWorld'
    print(a.indices(len(s))) #不越界的方法，适合不知道大小的情况下切片 #(5.10.2)
    for i in range(*a.indices(len(s))):
        print(s[i])

    items = [0, 1, 2, 3, 4, 5, 6]
    print(a.indices(len(items)))
    for i in range(*a.indices(len(items))):
        print(items[i])

# 序列中出现次数最多的元素
# 怎样找出一个序列中出现次数最多的元素呢？
from collections import Counter
# Counter 对象在几乎所有需要制表或者计数数据的场合是非常有用的工具。 在解决这类问题的时候你应该优先选择它，而不是手动的利用字典去实现。
def CollectionsCount():
    words = [
        'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
        'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
        'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
        'my', 'eyes', "you're", 'under'
    ]
    word_counts = Counter(words)
    print(word_counts)
    top_three = word_counts.most_common(3)
    print(top_three)
    print(word_counts['not'])

    #手动的方法
    morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes', 'why']
    # _word_counts = {}
    # for word in morewords:
    #     if checkDictHaveKey(_word_counts,word):
    #         _word_counts[word] += 1
    #     else:
    #         _word_counts[word] = 1
    # print(_word_counts['why']) #2
    for word in morewords:
        word_counts[word] += 1
    print(word_counts['eyes'])

    print("===============")
    # 实例一个鲜为人知的特性是它们可以很容易的跟数学运算操作相结合
    a = Counter(words)
    print(a)
    b = Counter(morewords)
    print(b)
    c = a + b  # 也算是合并表单增加次数的方法了
    print(c)
    d = b - a
    print(d)  #两个数据相减 #少于1的直接删除掉


# 通过某个关键字排序一个字典列表
# 你有一个字典列表，你想根据某个或某几个字典字段来排序这个列表
from operator import itemgetter
def SortDictionaryByKey(dirt = None ,reverseFlag = None):
    if dirt is None:
        dirt = [
            {'fname': 'Brian', 'lname': 'Jones', 'birthday': 19900101},
            {'fname': 'David', 'lname': 'Beazley', 'birthday': 20000102},
            {'fname': 'John', 'lname': 'Cleese', 'birthday': 19961001},
            {'fname': 'Big', 'lname': 'Jones', 'birthday': 19950601}
        ]
    if reverseFlag is None :
        reverseFlag = True

    #从小到大
    dirts_by_fname = sorted(dirt, key=itemgetter('fname'))
    #从大到小
    dirts_by_uid = sorted(dirt, key=itemgetter('birthday'), reverse = reverseFlag)
    print(dirts_by_fname)
    print(dirts_by_uid)
    #多个key 性别下沟通情况下 生日小到大
    # dirts_by_lfname = sorted(dirt, key=lambda r: (r['lname'],r['birthday'])) #lambda
    # 对性能要求比较高的话就使用 itemgetter() 方式
    dirts_by_lfname = sorted(dirt, key=itemgetter('lname', 'birthday'))
    print(dirts_by_lfname)

# 排序不支持原生比较的对象
# 你想排序类型相同的对象，但是他们不支持原生的比较操作（了解就好）
from operator import attrgetter
def SortDictionaryByFunc():
    class User:
        def __init__(self, user_id):
            self.user_id = user_id

        def __repr__(self):
            return 'User({})'.format(self.user_id)

    users = [User(23), User(3), User(99)]
    print(users)
    #print(sorted(users, key=lambda u: u.user_id))
    print(sorted(users, key=attrgetter('user_id')))

# 通过某个字段将记录分组
# 你有一个字典或者实例的序列，然后你想根据某个特定的字段比如 date 来分组迭代访问
# 一个非常重要的准备步骤是要根据指定的字段将数据排序。 因为 groupby() 仅仅检查连续的元素，如果事先并没有排序完成的话，分组函数将得不到想要的结果
from operator import itemgetter
from itertools import groupby
def groupDictionaryByValue(rows = None, data=None):
    if rows is None:
        rows = [
            {'address': '5412 N CLARK', 'date': '07/01/2012'},
            {'address': '5148 N CLARK', 'date': '07/04/2012'},
            {'address': '5800 E 58TH', 'date': '07/02/2012'},
            {'address': '2122 N CLARK', 'date': '07/03/2012'},
            {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
            {'address': '1060 W ADDISON', 'date': '07/02/2012'},
            {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
            {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
        ]
    # !!!一个非常重要的准备步骤是要根据指定的字段将数据排序。 因为 groupby() 仅仅检查连续的元素，如果事先并没有排序完成的话，分组函数将得不到想要的结果!!!
    rows.sort(key=itemgetter('date'))   #按日期排序
    # groupby 自动分组
    for date, items in groupby(rows, key=itemgetter('date')):
        print(date)
        for i in items:
            print(' ', i)

    print("加到一个列表方法")
    rows_by_date = defaultdict(list)
    for row in rows:
        rows_by_date[row['date']].append(row)   #在某key加值
    for r in rows_by_date['07/01/2012']:
        print(r)
        


# 过滤规则(是否数字)
def IsInt(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False

# 过滤序列元素
# 你有一个数据序列，想利用一些规则从中提取出需要的值或者是缩短序列
import math
from itertools import compress
def FilterOrderElement(order =None):
    if order is None:
        order = [1, 4, -5, 10, -7, 2, 3, -1]

    pos1 = (n for n in order if n > 0)
    pos2 = (n for n in order if n < 0)
    for x in pos1:
        print(x)
    print("===============")
    for x in pos2:
        print(x)
    print("==============")
    values = ['1', '2', '-3', '-', '4', 'N/A', '5']
    s_vale = filter(IsInt, values)  # filter函数->返回迭代器
    print(s_vale)
    l_vale = list(filter(IsInt, values)) #转LIST
    print(l_vale)

    #列表推导和生成器表达式通常情况下是过滤数据最简单的方式。 其实它们还能在过滤的时候转换数据
    mylist = [1, 4, -5, 10, -7, 2, 3, -1]
    print([math.sqrt(n) for n in mylist if n > 0])  #sqrt开根 求平方根函数

    #过滤操作的一个变种就是将不符合条件的值用新的值代替，而不是丢弃它们
    replaceList = clip_neg = [n if n > 0 else "x" for n in mylist]
    print(replaceList)

    #根据counts 过滤条件来筛选出addresses的数据
    addresses = [
        '5412 N CLARK',
        '5148 N CLARK',
        '5800 E 58TH',
        '2122 N CLARK',
        '5645 N RAVENSWOOD',
        '1060 W ADDISON',
        '4801 N BROADWAY',
        '1039 W GRANVILLE',
    ]
    counts = [0, 3, 10, 4, 1, 7, 6, 1]
    more5 = [n > 5 for n in counts]
    print(more5)
    m5 = list(compress(addresses, more5))
    print(m5)

# 从字典中提取子集
# 你想构造一个字典，它是另外一个字典的子集
def dictionaryGetSon():
    prices = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75
    }
    # Make a dictionary of all prices over 200
    p1 = {key: value for key, value in prices.items() if value > 200}
    print(p1)
    # Make a dictionary of tech stocks
    tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
    p2 = {key: value for key, value in prices.items() if key in tech_names}
    print(p2)

# 转换并同时计算数据
# 你需要在数据序列上执行聚集函数（比如 sum() , min() , max() ）， 但是首先你需要先转换或者过滤数据
import os
def changeData():
    nums = [1, 2, 3, 4, 5]
    s = sum(x * x for x in nums)
    print(s)

    files = os.listdir('.')
    if any(name.endswith('.py') for name in files):
        print('There be python!')
    else:
        print('Sorry, no python.')
    # Output a tuple as CSV
    s = ('ACME', 50, 123.45)
    print(','.join(str(x) for x in s))
    # Data reduction across fields of a data structure
    portfolio = [
        {'name': 'GOOG', 'shares': 50},
        {'name': 'YHOO', 'shares': 75},
        {'name': 'AOL', 'shares': 20},
        {'name': 'SCOX', 'shares': 65}
    ]
    min_shares = min(s['shares'] for s in portfolio)
    print(min_shares)
































