import pymysql
import requests
import xlrd

_workbook = xlrd.open_workbook(
    fr'C:\\Users\\BieFeNg\\Documents\\WeChat Files\\BieFeNg6\\FileStorage\\File\\2019-06\\原材料扣了产能(1).xlsx')

_sheet = _workbook.sheet_by_name("Sheet2")
rownum = _sheet.nrows
for rowx in range(rownum):
    data = _sheet.row_values(rowx)
    print(data[0])
    print(data[1])
    print(data[2])
    url = "http://web.myt11.com/catering/sku/doAdjust"

    payload = {"chgQty": "10", "skuId": 105830, "skuName": "澳洲安格斯谷饲西冷配薯条黑椒汁", "ckId": 3153, "tempQty": 11,
               "shopId": 12001}
    payload['skuId'] = int(data[0])
    payload['skuName'] = data[1]
    payload['chgQty']=int(data[2])
    headers = {
        'app': "nosession",
        'shopId': "12001",
        'Content-Type': "application/json",
    }

    # response = requests.request("POST", url, json=payload, headers=headers)
    # var = response.json()
    # if 'msg' in var:
    #     print(str(data[0]) + "\t" + data[1] + "\t" + var['msg'], end='')
    # else:
    #     print(str(data[0]) + "\t" + data[1] + "\t" + str(var), end='')
    # print("", end='\r\n')
