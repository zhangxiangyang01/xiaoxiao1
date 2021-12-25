# case覆盖率 90%
import requests
import json
class TestDepartment:

    def test_case_query1(self):

        # 分三步
        # 1 发送请求 获取数据
        res = requests.get('http://127.0.0.1:8000/api/departments/T001/')
        print(res)
        print(type(res))
        print(res.text)
        print(res.json())
        # 2 声明预期结果
        expect = '{"dep_id":"T001","dep_name":"Test学院xxxx","master_name":"Test-Masterx","slogan":null}'
        # 3 比较预期结果和实际结果之间的差异
        assert res.json() == json.loads(expect)
        # 断言两边都为字符串
        # 断言两边必须都为相同的格式

    def test_case_query2(self):
        # 分三步
        # 1 发送请求 获取数据
        res = requests.get('http://127.0.0.1:8000/api/departments/T002/')
        print(res)
        print(type(res))
        print(res.text)
        print(res.json())
        # 2 声明预期结果
        expect = '{"dep_id":"T001","dep_name":"Test学院xxxx","master_name":"Test-Masterx","slogan":null}'
        # 3 比较预期结果和实际结果之间的差异
        assert res.json() == json.loads(expect)
        # 断言两边都为字符串
    def test_case_add(self):
        # 这是上传到服务器的数据
        data = '{"data":[{"dep_id":"T014","dep_name":"Test学院xxxx","master_name":"Test-Masterx"}]}'
        # 定义headers
        headers = {"Content-type":"application/json"}
        res = requests.post('http://127.0.0.1:8000/api/departments/',data=data.encode('utf-8'),headers=headers)
        # 声明预期结果
        expect = '{"already_exist":{"count":0,"results":[]},"create_success":{"count":1,"results":[{"dep_id":"T014","dep_name":"Test学院xxxx","master_name":"Test-Masterx","slogan":null}]}}'
        # 比较
        assert  res.json() == json.loads(expect)
    def test_case_add1(self):
        # 这是上传到服务器的数据
        data = '{"data":[{"dep_id":"T015","dep_name":"Test学院xxxx","master_name":"Test-Masterx"}]}'
        # 定义headers
        headers = {"Content-type":"application/json"}
        res = requests.post('http://127.0.0.1:8000/api/departments/',data=data.encode('utf-8'),headers=headers)
        # 声明预期结果
        expect = '{"already_exist":{"count":0,"results":[]},"create_success":{"count":1,"results":[{"dep_id":"T015","dep_name":"Test学院xxxx","master_name":"Test-Masterx","slogan":null}]}}'
        # 比较
        assert  res.json() == json.loads(expect)