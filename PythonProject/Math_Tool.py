# -*- coding: utf-8 -*-
# @Time : 2020/2/12 19:12
# @Author : jjh
# @File : Math_Tool.py
# @Software: PyCharm
# @contact: 469672930@qq.com
# -*- 功能说明 -*-
# 数学工具
# -*- 功能说明 -*-

# 浮点数四舍五入
def MathFloor(num = None,fIndex = None):
    if num is None:
        num = 1.23
    if fIndex is None:
        fIndex = 1
    newNum = round(num,fIndex)
    return newNum


# 浮点数保留X位数字
def MathFloatRadixPoint(num = None,pIndex = None):
    if num is None:
        num = 1.2345
    if pIndex is None:
        pIndex = 3
    pStr = '{}{}{}'.format('0.', str(pIndex), 'f')
    newNum = format(num, pStr)
    return newNum


# 执行精确的浮点数运算
# 你需要对浮点数执行精确的计算操作，并且不希望有任何小误差的出现
from decimal import Decimal
from decimal import localcontext
def MathFloatResult(f1 = None,f2 = None,operatorStr = None,retainNum = None):
    if f1 is None:
        f1 = 1.3
    if f2 is None:
        f2 = 1.7
    if operatorStr is None:
        operatorStr = "/"
    if retainNum is None:
        retainNum = 3
    a = Decimal(f1)
    b = Decimal(f2)
    if operatorStr is "*" :
        return a * b    #日后再维护

    with localcontext() as ctx:
        ctx.prec = retainNum    #保留小数点
        return a / b


# 字节到大整数的打包与解包
# 你有一个字节字符串并想将它解压成一个整数。或者，你需要将一个大整数转换为一个字节字符串
def MathBigValueUnPack():
    # 将bytes解析为整数
    _bytes = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
    print(len(_bytes))
    print(int.from_bytes(_bytes, 'little'))
    print(int.from_bytes(_bytes, 'big'))

    # 将一个大整数转换为一个字节字符串
    x = 94522842520747284487117727783387188
    print(x.to_bytes(16, 'big'))
    print(x.to_bytes(16, 'little'))


# 复数的数学运算
# 你写的最新的网络认证方案代码遇到了一个难题，并且你唯一的解决办法就是使用复数空间。 再或者是你仅仅需要使用复数来执行一些计算操作
import cmath
def MathPlural():
    a = complex(2, 4)
    b = 3 - 5j
    print(a)
    print(b)
    print(a.real)
    print(a.imag)
    print(a.conjugate())
    # 如果要执行其他的复数函数比如正弦、余弦或平方根，使用 cmath 模块
    print("==============")
    print(cmath.sin(a))
    print(cmath.cos(a))
    print(cmath.exp(a))
    value = cmath.sqrt(-1) # 果你想生成一个复数返回结果，你必须显示的使用 cmath 模块
    return  value