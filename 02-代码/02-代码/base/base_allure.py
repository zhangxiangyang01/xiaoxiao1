import allure


def add_description(res, em):
    # 为模型增加实际结果的属性，方便报告的产生
    em.actual_res = res.text
    em.actual_status_code = res.status_code

    # 处理报告
    allure.dynamic.title(em.module_name + "-" + em.title)

    table_header = """<h1>Test with some complicated html description</h1>
           <table style="width:100%%">
             <tr>
               <th>名称</th>
               <th>值</th>
             </tr>
             %s
           </table>"""

    table_content_item = """
                     <tr align="center">
                        <td>%s</td>
                        <td>%s</td>
                     </tr>
                   """

    table_content = ""
    for k, v in em.__dict__.items():
        table_content += table_content_item % (k, v)
    table = table_header % table_content
    allure.dynamic.description_html(table)