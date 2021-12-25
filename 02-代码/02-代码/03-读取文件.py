import json

# 文件的读
with open('data.png','r') as f:
    # 将文件的内容转换为对象
    res = json.load(f)
    print(res)
    print(type(res))



# # 文件写
# data = {
#     'name':'zhangsan',
#     'age':18,
#     'height':None
# }
# with open('data1.json','w') as f:
#
# # 将对象转字符串的
#     json.dump(data,f)