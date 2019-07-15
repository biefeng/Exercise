import requests

headers = {
    'sid': '7c4215eeed194d8cb0a2e57e11bb9231',
    'shopId': '12001'
}
url = "http://172.16.1.33:80/pmc-prod/storeSku/list"
count = 0;
for i in range(5):
    i += 1;
    param = {"skuId": None, "brandId": "", "tempBizStatus": None, "category": "餐配酒水 ... ...", "categoryIdStr": "",
             "categoryId4List": "739,740,741,742,743,744,745,746,747,748,749,750,751,752,753,754", "buyer": "",
             "productName": "", "upcCodes": "", "type": None, "dataStatus": None, "storeId": 12001, "pageNo": i,
             "pageSize": 10, "shopId": '12001'}
    response = requests.post(url=url, data=param, headers=headers)
    response.encoding = 'utf-8'

    list = response.json()['data']['list']

    for data in list:
        count += 1
        print(data['skuId'], end=",")

print(count)
