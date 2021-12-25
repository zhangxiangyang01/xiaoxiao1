class People:

    def __init__(self):
        self.name = "xiaoming"
        self.age = 18
        self.height = 175


p = People()

for k, v in p.__dict__.items():
    print(k)
    print(v)

# import traceback
#
# def c():
#     print(traceback.extract_stack())
#     print("hello")
#
# def b():
#     c()
#
#
# def a():
#     b()
#
#
# # 需求 如果是 a 调用 ，正常打印
# # 需求 如果是 c 调用 ，不打印
#
# a()
#
# c()
#
#
#
# # a = "add_001\nadd_002\nadd_003\tadd_004\radd_005"
# #
# # print(a.split())
# #
# #
# # # "add", "100"
# # #
# # # [add_001, add_002 .... add_100]
# #
# # # "update", "5"
# # #
# # # [update_001, update_001 .... update_005]
# #
# # # def hello(prefix, count):
# # #     temp = list()
# # #     for i in range(count):
# # #         temp.append("%s_%03d" % (prefix, i + 1))
# # #
# # #     return temp
# # #
# # #
# # # print(hello("update", 5))
# #
# # # a = "import random"
# # # exec(a)
# # #
# # # b = "print(random.randint(1, 5))"
# # # eval(b)
# #
# #
# # # a = '{1, 2, 3}'
# # #
# # # import json
# # #
# # # a = eval(a)
# # #
# # #
# # #
# # # print(a)
# # # print(type(a))
# #
# #
# # # # a = '{"age": 18, "name": "xiaoming"}'
# # # a = '{1, 2, 3}'
# # #
# # #
# # # import json
# # #
# # # a = json.loads(a)
# # # print(a)
# # # print(type(a))
# #
# #
# # # a = ["add_001", "add_002", "query_001"]
# # # #
# # # # temp_list = list()
# # # # for i in a:
# # # #     if i.startswith("add"):
# # # #         print(i)
# # # #         temp_list.append(i)
# # # #
# # # # print(temp_list)
# # # #
# # # #
# # # # # class People:
# # # #
# # # #     def __init__(self):
# # # #         self.name = ""
# # # #         self.age = 0
# # # #
# # # #
# # # # xiaoming = People()
# # # # xiaoming.name = "小明"
# # # # xiaoming.age = 18
# # # #
# # # # xiaohong = People()
# # # # xiaohong.name = "小红"
# # # # xiaohong.age = 16
# # # #
# # # # def say_hello(p):
# # # #     print("%s今年 %d 岁" % (p.name, p.age))
# # # #
# # # # # def say_hello(temp_dict):
# # # # #     print("%s今年 %d 岁" % (temp_dict["name"], temp_dict["age"]))
# # # # #
# # # # # xiaoming = {"name": "xiaoming", "age": 18}
# # # # # say_hello(xiaoming)
# # # #
# # # # #
# # # # # class TestDepartment:
# # # # #     def get_case_id(self,count,prefix):
# # # # #          # 定义一个列表
# # # # #         ids = list()
# # # # #         for i in range(count):
# # # # #             ids.append('%s_%03d' %(prefix,i+1))
# # # # #
# # # # #         print(ids)
# # # # #
# # # # #
# # # # #
# # # # # #
# # # # # #
# # # # # # if __name__ == '__main__':
# # # # # #     TestDepartment().get_case_id(5,'query')
# # # # #
# # # # # ids = list()
# # # # # for i in range(5):
# # # # #     ids.append('add_%03d' %(i+1))
# # # # #     print(ids)
