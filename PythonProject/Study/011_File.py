# 访问模式	说明
# r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
# w	打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
# rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
# wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
# r+	打开一个文件用于读写。文件指针将会放在文件的开头。
# w+	打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
# rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
# wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。


#备份文件
# 提示输入文件
# oldFileName = input("请输入要拷贝的文件名字:")
#
# # 以读的方式打开文件
# oldFile = open(oldFileName,'rb')
#
# # 提取文件的后缀
# fileFlagNum = oldFileName.rfind('.')
# if fileFlagNum > 0:
#     fileFlag = oldFileName[fileFlagNum:]
#
# # 组织新的文件名字
# newFileName = oldFileName[:fileFlagNum] + '[复件]' + fileFlag
#
# # 创建新文件
# newFile = open(newFileName, 'wb')
#
# # 把旧文件中的数据，一行一行的进行复制到新文件中
# for lineContent in oldFile.readlines():
#     newFile.write(lineContent)
#
# # 关闭文件
# oldFile.close()
# newFile.close()
#
# f = open('test.txt', 'w')
# f.write('-hello world, i am here!')
# f.close()

import os
#os.rename("test.txt", "test-最终版.txt")

flag = os.path.exists("张三")
if flag == False :
    os.mkdir("张三")
name = os.getcwd()  #获取当前目录
mkName = name + '\\张三'
os.chdir(mkName)
# flag = os.path.exists("test.txt")
# if flag == False :
#     f = open('test.txt', 'a')
# else :
#     f = open('test.txt')
f = open('test.txt', 'a')
f.writelines('hello world, i am here!')
f.close()