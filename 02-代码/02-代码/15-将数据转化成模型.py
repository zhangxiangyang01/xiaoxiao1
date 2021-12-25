import json
import requests
from base import base_excel
import pytest


class TestDepartment:

    BASE_URL = 'http://127.0.0.1:8000'

    # 接口的增
    @pytest.mark.parametrize("case_id", ["add_001", "add_002", "add_003", "add_004", "add_005"])
    def test_case_add(self, case_id):
        # 获取Excel表格中的数据
        em = base_excel.get_item_with_case_id(case_id)
        # 分三步
        # 1 发送请求 获取数据
        res = requests.post(self.BASE_URL + em.url, data=em.data.encode('utf-8'), headers=json.loads(em.headers))
        # 2 声明预期结果
        expect = em.expect_res
        # 3 比较预期结果和实际结果之间的差异
        assert res.json() == json.loads(expect)
        # 断言两边都为字符串
        # 断言两边必须都为相同的格式

    # 实现参数化
    # 接口的查
    @pytest.mark.parametrize('case_id', ["query_001", 'query_002', "query_003", 'query_004', 'query_005'])
    def test_case_query(self, case_id):
        # 获取Excel表格中的数据
        em = base_excel.get_item_with_case_id(case_id)
        # 分三步
        # 1 发送请求 获取数据
        res = requests.get(self.BASE_URL + em.url)

        # 2 声明预期结果
        expect = em.expect_res
        # 3 比较预期结果和实际结果之间的差异
        if em.expect_way == "json":
            assert res.json() == json.loads(expect)
        elif em.expect_way == 'status_code':
            assert res.status_code == expect
        # 断言两边都为字符串
        # 断言两边必须都为相同的格式

    # 接口的改
    @pytest.mark.parametrize("case_id", ['update_001', "update_002"])
    def test_case_update(self, case_id):
        # 获取Excel表格中的数据
        em = base_excel.get_item_with_case_id(case_id)

        # 分三步
        res = requests.put(self.BASE_URL + em.url, data=em.data.encode('utf-8'), headers=json.loads(em.headers))
        # 2 声明预期结果
        expect = em.expect_res
        # 3 比较预期结果和实际结果之间的差异

        if em.expect_way == "json":
            assert res.json() == json.loads(expect)
        elif em.expect_way == 'status_code':
            assert res.status_code == expect
