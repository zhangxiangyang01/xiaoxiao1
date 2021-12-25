import json
import requests
from base import base_excel
from base.base_assert import assert_res
import pytest


class TestDepartment:

    BASE_URL = 'http://127.0.0.1:8000'

    # @pytest.mark.parametrize("name", ["zhangsan", "lisi", "wangwu", "zhaoli"])
    # def test_hello1(self, name):
    #     print("%s - hello" % name)

    # def test_hello2(self):
    #     print("lisihello")
    #
    # def test_hello3(self):
    #     print("wangwuhello")

    # @pytest.mark.parametrize("case_id", ["add_001", "add_002"])
    # def test_add_001(self, case_id):
    #     em = base_excel.get_item_with_case_id(case_id)
    #     requests.post(self.BASE_URL + em.url, headers=json.loads(em.headers), data=em.data.encode("utf-8"))
    #
    # def test_add_002(self):
    #     em = base_excel.get_item_with_case_id("add_002")
    #     requests.post(self.BASE_URL + em.url, headers=json.loads(em.headers), data=em.data.encode("utf-8"))

    # 接口的增
    @pytest.mark.parametrize("case_id", ["add_001", "add_002", "add_003", "add_004", "add_005"])
    def test_case_add(self, case_id):
        # 获取Excel表格中的数据
        em = base_excel.get_item_with_case_id(case_id)
        # 分三步
        # 1 发送请求 获取数据
        res = requests.post(self.BASE_URL + em.url, data=em.data.encode('utf-8'), headers=eval(em.headers))
        # 3 比较预期结果和实际结果之间的差异
        assert_res(res, em)
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

        # 3 比较预期结果和实际结果之间的差异
        assert_res(res, em)
        # 断言两边都为字符串
        # 断言两边必须都为相同的格式

    # 接口的改
    @pytest.mark.parametrize("case_id", ['update_001', "update_002"])
    def test_case_update(self, case_id):
        # 获取Excel表格中的数据
        em = base_excel.get_item_with_case_id(case_id)

        # 分三步
        res = requests.put(self.BASE_URL + em.url, data=em.data.encode('utf-8'), headers=eval(em.headers))

        # 3 比较预期结果和实际结果之间的差异
        assert_res(res, em)
