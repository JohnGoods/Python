namesList = ['xiaoWang','xiaoZhang','xiaoHua']
for name in namesList:
    print(name)

A = ['xiaoWang','xiaoZhang','xiaoHua']
print("-----添加之前，列表A的数据-----")
for tempName in A:
    print(tempName)

#提示、并添加元素
temp = input('请输入要添加的学生姓名:')
A.append(temp)      #重点
A.insert(0,"test")
print("-----添加之后，列表A的数据-----")
for tempName in A:
    print(tempName)

#获取用户要查找的名字
findName = "test"
if findName in A:
    print('在字典中找到了相同的名字')
else:
    print('没有找到')

print('--------------------')
#删除元素("删"del, pop, remove)
print('del------删除之前------')
for tempName in A:
    print(tempName)
del A[2]
print('------删除之后------')
for tempName in A:
    print(tempName)
print('--------------------')

print('pop------删除之前------')
for tempName in A:
    print(tempName)
A.pop()
print('------删除之后------')
for tempName in A:
    print(tempName)

print('--------------------')
print('remove------删除之前------')
for tempName in A:
    print(tempName)
A.remove('test')
print('------删除之后------')
for tempName in A:
    print(tempName)

print('---------排序-----------')
def takeSecond(elem):
    return elem[1]
numList = [[1,2],[1,3],[1,5],[1,1],[1,12],[1,44],[1,7],[1,6]]
numList.sort(key=takeSecond,reverse=True)  #key对比元素  #reverse是否降序
for i in numList:
    print(i)