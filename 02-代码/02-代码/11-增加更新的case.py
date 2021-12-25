import json
import requests
from  base import base_excel
import pytest



class TestDepartment:
    Base_url = 'http://127.0.0.1:8000'


    # 接口的增
    @pytest.mark.parametrize("case_id", ["add_001", "add_002", "add_003", "add_004", "add_005"])
    def test_case_add(self, case_id):
        # 获取行
        rows = base_excel.get_rows_number_with_case_id(case_id)
        # 获取行的具体内容
        values = base_excel.get_rows_value(rows)
        print(values)
        # 模块
        model_name = values[0]
        # 用例编号
        case_id = values[1]
        # 标题
        title = values[2]
        # 前置条件
        fixture = values[3]
        url = values[4]
        method = values[5]  # 请求方法
        data = values[6]  # 数据
        cookie = values[7]  # cookie
        headers = values[8]  # headers
        expect_way = values[9]  # 预期结果的方式
        expect_res = values[10]  # 预期结果

        # 分三步
        # 1 发送请求 获取数据
        res = requests.post(self.Base_url + url, data=data.encode('utf-8'), headers=json.loads(headers))

        # 2 声明预期结果
        expect = expect_res
        # 3 比较预期结果和实际结果之间的差异
        assert res.json() == json.loads(expect)
        # 断言两边都为字符串
        # 断言两边必须都为相同的格式
    # 实现参数化
    # 接口的查
    @pytest.mark.parametrize('case_id',["query_001",'query_002',"query_003",'query_004','query_005'])
    def test_case_query(self,case_id):

        # 获取行
        rows = base_excel.get_rows_number_with_case_id(case_id)
        # 获取行的具体内容
        values = base_excel.get_rows_value(rows)
        print(values)
        # 模块
        model_name = values[0]
        # 用例编号
        case_id = values[1]
        # 标题
        title = values[2]
        # 前置条件
        fixture = values[3]
        url = values[4]
        method = values[5] # 请求方法
        data = values[6] # 数据
        cookie = values[7] # cookie
        headers = values[8] # headers
        expect_way = values[9] # 预期结果的方式
        expect_res = values[10] # 预期结果


        # 分三步
        # 1 发送请求 获取数据
        res = requests.get(self.Base_url + url)

        # 2 声明预期结果
        expect = expect_res
        # 3 比较预期结果和实际结果之间的差异
        assert res.json() == json.loads(expect)
        # 断言两边都为字符串
        # 断言两边必须都为相同的格式
    # 接口的改
    @pytest.mark.parametrize("case_id",['update_001',"update_002"])
    def test_case_update(self,case_id):
        # 获取行
        rows = base_excel.get_rows_number_with_case_id(case_id)
        # 获取行的具体内容
        values = base_excel.get_rows_value(rows)
        print(values)
        # 模块
        model_name = values[0]
        # 用例编号
        case_id = values[1]
        # 标题
        title = values[2]
        # 前置条件
        fixture = values[3]
        url = values[4]
        method = values[5]  # 请求方法
        data = values[6]  # 数据
        cookie = values[7]  # cookie
        headers = values[8]  # headers
        expect_way = values[9]  # 预期结果的方式
        expect_res = values[10]  # 预期结果


        # 分三步
        res =   requests.put(self.Base_url+url,data=data.encode('utf-8'),headers= json.loads(headers))
        # 2 声明预期结果
        expect = expect_res
        # 3 比较预期结果和实际结果之间的差异
        assert res.json() == json.loads(expect)
