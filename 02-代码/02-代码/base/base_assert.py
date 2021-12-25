import json
import traceback
import os

def assert_res(res, em):

    # 如果这个断言是自己调用的，则不进行后续的断言操作
    if os.getcwd() in traceback.extract_stack()[-3][0]:
        return

    if em.expect_way == "json":
        assert res.json() == json.loads(em.expect_res)
    elif em.expect_way == 'status_code':
        assert res.status_code == em.expect_res
