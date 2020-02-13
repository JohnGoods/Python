name = "jiangjianghao"
sum = 0
for s in name:
    print(s)
for i in range(101):
    sum = sum + i
    print(i)
    if i == 100:
        print("sum---->%d"%sum)

#练习题
print("=====================")
s = 'Hello World!'
print(s)
print("=====================")
reSult = s[::-1]
print(reSult)
print("=====================")
newSult = ""
max_index = len(reSult)-1
for index,value in enumerate(reSult):
    #print(index,value)
    newSult += reSult[max_index - index]
print(newSult)
print("=====================")