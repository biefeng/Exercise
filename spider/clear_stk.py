import pymysql
import requests
import xlrd

_workbook = xlrd.open_workbook(
    fr'C:\\Users\\BieFeNg\\Documents\\WeChat Files\\BieFeNg6\\FileStorage\\File\\2019-06\\餐饮自动清零 商品(1).xlsx')

_sheet = _workbook.sheet_by_name("Sheet1")
rownum = _sheet.nrows
headers = {
    'sid': "40c99f6eab684679a7f83557e0ebc136",
    'shopId': "12001",
    'Content-Type': "application/json"
}
for rowx in range(rownum):
    data = _sheet.row_values(rowx)
    payload = {"skuId": "", "opt": "", "isAuthSql": 1, "pageNo": 1, "pageSize": 10, "isCatering": "", "isProcess": "",
               "skuName": "", "upcCodes": "", "ckId": "", "shopId": 12001}

    payload['skuId'] = str(data[1])[:6]
    response = requests.post(url='http://web.myt11.com/catering/sku/listData', json=payload, headers=headers)
    json = response.json()
    var = json['data']['list'][0]
    if 'availableQty' in var:
        qty = -var['availableQty']
        print(qty)
        payload = {"chgQty": "10", "skuId": 105830, "skuName": "澳洲安格斯谷饲西冷配薯条黑椒汁", "ckId": 3153, "tempQty": 11}
        payload['chgQty'] = str(qty)
        payload['skuId'] = str(data[1])[:6]
        headers_1 = {
            'app': 'nosession',
            'shopId': '12001',
            'Content-Type': "application/json",
        }
        result = requests.post(url='http://web.myt11.com/catering/sku/doAdjust', json=payload, headers=headers)
        var1 = result.json()
        print(var1)
        break
