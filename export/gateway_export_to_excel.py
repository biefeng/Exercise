# -*- coding:utf-8 -*-
# author : BieFeNg
# date_time 2020/08/10 11:11
# file_name : gateway_export_to_excel.py

import requests
from xlwt import *


def export_data_to_excel():
    index = 1
    page_size = 15
    total = 0

    work_book = Workbook(encoding="ascii")
    center_alignment = Alignment()
    center_alignment.horz = Alignment.HORZ_RIGHT
    center_alignment.vert = Alignment.VERT_CENTER

    border = Borders()
    border.top = Borders.THIN
    border.left = Borders.THIN
    border.bottom = Borders.THIN
    border.right = Borders.THIN

    head_style = XFStyle()

    head_pattern = Pattern()
    head_pattern.pattern = Pattern.SOLID_PATTERN
    head_pattern.pattern_fore_colour = Style.colour_map['gray25']

    head_style.pattern = head_pattern

    head_font = Font()
    head_font.bold = True
    head_style.font = head_font

    head_style.alignment = center_alignment
    head_style.borders = border

    data_style = XFStyle()
    data_style.alignment = center_alignment
    data_style.borders = border
    work_sheet = work_book.add_sheet("Sheet1")
    header = ['app_name', "service_name", "method_name/path", "alias"]
    for i, h in enumerate(header):
        work_sheet.write(0, i, h, data_style)
    row = 1
    while True:
        url = "http://gateway-web.myt11.com/gateway/config/listData"

        payload = "{\"pageNo\":%s,\"pageSize\":%s}" % (index, page_size)

        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
            'Content-Type': 'application/json',
            'Origin': 'http://gateway-web.myt11.com',
            'Referer': 'http://gateway-web.myt11.com/gateway/config/index',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Cookie': 'session_name=e5338ca650954ca18f7e34e69b023f31; ssoValidCode=494b77989a85ca9f5c53069156c18f2e; sso_user_info=31a75f60f7357228543b6bc350ba505f; sso_session_start_time=1597023392689; sso_user_button_info=5c0e23e0e869f845dbb7138a625d3b90; sso_user_menu_info=9cbf432144984a5797f529a677109b32; sso_all_button_code_info=f165c0fe80d07c67640939bf1b89ce49; pin=uvmt.yrv'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        res = response.json()
        registry_list = res['data']
        for registry in registry_list:
            alias_ = registry['alias']
            app_name_ = registry['appName']
            full_interface_ = registry['fullInterface']
            method_name_ = registry["methodName"]
            work_sheet.write(row, 0, app_name_, data_style)
            work_sheet.write(row, 1, full_interface_, data_style)
            work_sheet.write(row, 2, method_name_, data_style)
            work_sheet.write(row, 3, alias_, data_style)
            row += 1
        total = res['count']
        if index > 1 and (index - 1) * page_size >= total:
            break
        index += 1

    work_book.save("C:\\Users\\33504\\Desktop\\gateway_shop.xls")


export_data_to_excel()
