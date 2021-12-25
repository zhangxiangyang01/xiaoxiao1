import json
import requests
from  base import base_excel
import pytest

class TestDepartment:
    Base_url = 'http://127.0.0.1:8000'

    # python 有个特点，当给某个对象的某个属性赋值的时候，如果没有这个属性就会创建
    # 先调用的getdata，这个方法就是在给 self.case_data 属性赋值，它发现没有就会创建，然后getdata后面去调用 self.case_data 就可以拿到了。
    def get_data(self,case_id):
        rows = base_excel.get_rows_number_with_case_id(case_id)
        # 获取行的具体内容
        values = base_excel.get_rows_value(rows)
        print(values)
        # 模块
        self.model_name = values[0]
        # 用例编号
        self.case_id = values[1]
        # 标题
        self.title = values[2]
        # 前置条件
        self.fixture = values[3]
        self.url = values[4]
        self.method = values[5]  # 请求方法
        self.data = values[6]  # 数据
        self.cookie = values[7]  # cookie
        self.headers = values[8]  # headers
        self.expect_way = values[9]  # 预期结果的方式
        self.expect_res = values[10]  # 预期结果

    # 接口的增
    @pytest.mark.parametrize("case_id", ["add_001", "add_002", "add_003", "add_004", "add_005"])
    def test_case_add(self, case_id):
        # 获取Excel表格中的数据
        self.get_data(case_id)
        # 分三步
        # 1 发送请求 获取数据
        res = requests.post(self.Base_url + self.url, data=self.data.encode('utf-8'), headers=json.loads(self.headers))
        # 2 声明预期结果
        expect = self.expect_res
        # 3 比较预期结果和实际结果之间的差异
        assert res.json() == json.loads(expect)
        # 断言两边都为字符串
        # 断言两边必须都为相同的格式
    # 实现参数化
    # 接口的查
    @pytest.mark.parametrize('case_id',["query_001",'query_002',"query_003",'query_004','query_005'])
    def test_case_query(self,case_id):

        self.get_data(case_id)
        # 分三步
        # 1 发送请求 获取数据
        res = requests.get(self.Base_url + self.url)

        # 2 声明预期结果
        expect = self.expect_res
        # 3 比较预期结果和实际结果之间的差异
        assert res.json() == json.loads(expect)
        # 断言两边都为字符串
        # 断言两边必须都为相同的格式
    # 接口的改
    @pytest.mark.parametrize("case_id",['update_001',"update_002"])
    def test_case_update(self,case_id):
        # 获取行
        self.get_data(case_id)

        # 分三步
        res =   requests.put(self.Base_url+self.url,data=self.data.encode('utf-8'),headers= json.loads(self.headers))
        # 2 声明预期结果
        expect = self.expect_res
        # 3 比较预期结果和实际结果之间的差异
        assert res.json() == json.loads(expect)
