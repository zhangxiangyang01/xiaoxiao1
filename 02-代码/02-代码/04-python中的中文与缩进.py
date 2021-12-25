import  json

# 定义字典
data = {

    'name':'张三',
    'age':18,
    'heigth':None
}

res = json.dumps(data,ensure_ascii=False,indent=4)

print(res)