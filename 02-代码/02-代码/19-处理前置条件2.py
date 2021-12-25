import json
import requests
from base import base_excel
from base.base_assert import assert_res
import pytest


def get_case_id(prefix, count):
    temp = list()
    for i in range(count):
        temp.append("%s_%03d" % (prefix, i + 1))

    return temp


class TestDepartment:
    BASE_URL = 'http://127.0.0.1:8000'

    def deal_fixture(self, em):
        fixture = em.fixture
        if fixture is not None:
            for fixture_case_id in fixture.split():
                if fixture_case_id.startswith("add"):
                    self.test_case_add(fixture_case_id)
                elif fixture_case_id.startswith("query"):
                    self.test_case_query(fixture_case_id)
                elif fixture_case_id.startswith("update"):
                    self.test_case_update(fixture_case_id)

    # 接口的增
    @pytest.mark.parametrize("case_id", get_case_id("add", 5))
    def test_case_add(self, case_id):
        # 1. 获取Excel表格中的数据
        em = base_excel.get_item_with_case_id(case_id)
        # 2. 处理前置
        self.deal_fixture(em)
        # 3. 发送请求
        res = requests.post(self.BASE_URL + em.url, data=em.data.encode('utf-8'), headers=eval(em.headers))
        # 4. 断言
        assert_res(res, em)

    # 实现参数化
    # 接口的查
    @pytest.mark.parametrize('case_id', get_case_id("query", 5))
    def test_case_query(self, case_id):
        # 1. 获取Excel表格中的数据
        em = base_excel.get_item_with_case_id(case_id)
        # 2. 处理前置
        self.deal_fixture(em)
        # 3. 发送请求
        res = requests.get(self.BASE_URL + em.url)
        # 4. 断言
        assert_res(res, em)

    # 接口的改
    @pytest.mark.parametrize("case_id", get_case_id("update", 2))
    def test_case_update(self, case_id):
        # 1. 获取Excel表格中的数据
        em = base_excel.get_item_with_case_id(case_id)
        # 2. 处理前置
        self.deal_fixture(em)
        # 3. 发送请求
        res = requests.put(self.BASE_URL + em.url, data=em.data.encode('utf-8'), headers=eval(em.headers))
        # 4. 断言
        assert_res(res, em)
