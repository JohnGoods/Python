#  def foxi(num1,num2):
#     return num1+num2
# print(foxi(1,2))
# print("======")
# print(foxi(1,3))

numTest = 0
def num1():
    return 100
def num2():
    value = num1()
    numTest = value
    print(numTest)
num2()
print(numTest)

def divid(a, b):
    shang = a//b
    yushu = a%b
    return shang, yushu  #默认是元组

result = divid(5, 2)
print(result)  # 输出(2, 1)

def printinfo(name, age=35):
   # 打印任何传入的字符串
   print("name: %s" % name)
   print("age %d" % age)

# 调用printinfo函数
printinfo(name="miki")  # 在函数执行过程中 age去默认值35
printinfo(age=9 ,name="miki")


def get_my_info():
    high = 178
    weight = 100
    age = 18
    return high, weight, age


# result = get_my_info()
# print(result)

my_high, my_weight, my_age = get_my_info()
print(my_high)
print(my_weight)
print(my_age)

print("======")
g = lambda x:x+1
print(g(100))


stus = [
    {"name": "zhangsan", "age": 18},
    {"name": "lisi", "age": 19},
    {"name": "wangwu", "age": 17}
]
stus.sort(key = lambda x: x['age'],reverse=False)

for x in stus:
    print(x)
print("======")
list = [x for x in range(4) if x%2 == 0]    #- -
for x in list:
    print(x)
print("======")