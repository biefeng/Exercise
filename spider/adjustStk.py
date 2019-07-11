import pymysql
import requests

connection = pymysql.connect(host="172.16.1.106", user="root", password="JY@myt11", database="jy_catering")

cursor = connection.cursor(cursor=pymysql.cursors.DictCursor)
sql = 'SELECT sku_id skuId ,sku_name skuName,ck_id ckId FROM catering_sku WHERE shop_id = 12001 AND is_catering=1 and sku_type=1  AND ck_id IS NOT null '

cursor.execute(sql)

result = cursor.fetchall()

for data in result:
    url = "http://web.myt11.com/catering/sku/doAdjust"

    payload = {"chgQty": "11", "skuId": 105830, "skuName": "澳洲安格斯谷饲西冷配薯条黑椒汁", "ckId": 3153, "tempQty": 11,
               "shopId": 12001}
    payload['ckId'] = data['ckId']
    payload['skuId'] = data['skuId']
    payload['skuName'] = data['skuName']
    headers = {
        'app': "nosession",
        'shopId': "12001",
        'Content-Type': "application/json",
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    var = response.json()
    if 'msg' in var:
        print(str(data['skuId']) + "\t" + data['skuName'] + "\t" + var['msg'], end='')
    else:
        print(str(data['skuId']) + "\t" + data['skuName'] + "\t" + str(var), end='')
    print("", end='\r\n')
