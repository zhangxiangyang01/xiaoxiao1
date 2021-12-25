from base import base_excel



# case覆盖率 90%
import requests
import json
class TestDepartment:

    def test_case_query1(self):
        # 获取多少行
       rows = base_excel.get_rows()
       print(rows) #11行
        # 获取多少列
       cols = base_excel.get_columns()
       print(cols) # 14列
       # 获取行数据
       values = base_excel.get_rows_value(2)
       print(values)

    # 获取列数据
       col_values = base_excel.get_columns_value('A')
       print(col_values)
       base_excel.excel_write_data(2,14,'hello')
