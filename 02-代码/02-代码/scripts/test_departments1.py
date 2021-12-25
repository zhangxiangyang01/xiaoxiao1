import json

import allure
import requests
from base import base_excel
from base.base_allure import add_description
from base.base_assert import assert_res
import pytest


def get_case_id():

    return base_excel.get_columns_value("b")[1:]

def get():
    print("调用 get")
    return "hello"

def post():
    print("调用 post")
    return "hello"


class TestDepartment:
    BASE_URL = 'http://127.0.0.1:8000'

    # 接口的增
    @pytest.mark.parametrize("case_id", get_case_id())
    def test_case(self, case_id):



        # 1. 获取Excel表格中的数据
        em = base_excel.get_item_with_case_id(case_id)
        # 3. 发送请求

        print(em.method.lower())

        res = eval("%s()" % em.method.lower())

        print(res)
        #     res = post()
        # if case_id.startswith("query"):
        #     res = get()

        # # 4. 处理报告
        # add_description(res, em)
        # # 5. 断言
        # assert_res(res, em)
