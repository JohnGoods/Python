#coding=utf-8
# 批量在文件名前加前缀
import os
zidingyiName = "批量后缀_"
fileName = "批量重命名文件夹"

funFlag = 1 # 1表示添加标志  2表示删除标志
name = os.getcwd()  #获取当前目录
pathName = name + '\\' + fileName + '\\'    #路径
delPathName = name + '\\' + fileName    #删除路径

flag = os.path.exists(pathName)
if flag == True:
    # 获取指定路径的所有文件名字
    dirList = os.listdir(pathName)
    i = 0
        # 遍历输出所有文件名字
    for name in dirList:
        # print (name)
        fileFlagNum = name.rfind('.')
        if fileFlagNum > 0:
            _fileFlag = name[fileFlagNum:]
        if funFlag == 1:
            newName = zidingyiName + str(i) + _fileFlag
        elif funFlag == 2:
            num = len(zidingyiName)
            newName = name[num:]
        # print(newName)
        i = i + 1
        flag = os.path.exists(pathName + newName)
        if flag == True:
            continue
        os.rename(pathName + name, pathName + newName)
else:
    os.mkdir(fileName)
    name = os.getcwd()  # 获取当前目录
    mkName = name + '\\' + fileName
    os.chdir(mkName)
    for x in range(100):
        f = open(str(x+1)+'test.jpg', 'a')
        #f.writelines('hello world, i am here!')
        f.close()