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

