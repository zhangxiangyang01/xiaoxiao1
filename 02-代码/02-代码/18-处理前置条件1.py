import json
import requests
from base import base_excel
from base.base_assert import assert_res
from base.base_fixture import deal_fixture
import pytest


def get_case_id(prefix, count):
    temp = list()
    for i in range(count):
        temp.append("%s_%03d" % (prefix, i + 1))

    return temp

class TestDepartment:

    BASE_URL = 'http://127.0.0.1:8000'

    # 接口的增
    @pytest.mark.parametrize("case_id", get_case_id("add", 5))
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
    @pytest.mark.parametrize('case_id', get_case_id("query", 5))
    def test_case_query(self, case_id):
        # 获取Excel表格中的数据
        em = base_excel.get_item_with_case_id(case_id)

        deal_fixture(self, em)

        # for fixture_case_id in em.fixture.split():
        #     if fixture_case_id.startswith("add"):
        #         self.test_case_add(fixture_case_id)
        #     elif fixture_case_id.startswith("query"):
        #         self.test_case_query(fixture_case_id)
        #     elif fixture_case_id.startswith("update"):
        #         self.test_case_update(fixture_case_id)

        # 分三步
        # 1 发送请求 获取数据
        res = requests.get(self.BASE_URL + em.url)

        # 3 比较预期结果和实际结果之间的差异
        assert_res(res, em)
        # 断言两边都为字符串
        # 断言两边必须都为相同的格式

    # 接口的改
    @pytest.mark.parametrize("case_id", get_case_id("update", 2))
    def test_case_update(self, case_id):
        # 获取Excel表格中的数据
        em = base_excel.get_item_with_case_id(case_id)

        # 分三步
        res = requests.put(self.BASE_URL + em.url, data=em.data.encode('utf-8'), headers=eval(em.headers))

        # 3 比较预期结果和实际结果之间的差异
        assert_res(res, em)
