import  json

# 定义字典
data = {

    'name':'zhangsan',
    'age':18,
    'heigth':None
}
# 将字典转为字符串
res = json.dumps(data)
print(res)
# 将字符串转为对象
obj = json.loads(res)
print(obj)
print(type(obj))