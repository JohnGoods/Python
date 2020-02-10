info = {"name":"test","num":123,"id":11}
print(info["name"])
print(info["num"])
age = info.get('age',100)
print(age)
if info.get('age'): #重点
    print(info["age"])
print('--------------------')
info = {'name':'班长', 'id':100, 'sex':'f', 'address':'地球亚洲中国北京'}
newId = int(input('请输入新的学号'))
info["id"] = newId
for x in info:
    print(x,"+",info[x])
print("删除前")
print("删除后")
del info["id"]
for x in info:
    print(x,"+",info[x])
info.clear()