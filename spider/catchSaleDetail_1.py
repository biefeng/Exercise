# -* encoding:utf-8 *-

import requests
import csv

headers = {
    'sid': '2c266c02977d483fad796a0ffa309c7f',
    'Content-Type': 'application/json;charset=UTF-8'
}

url = "http://web.myt11.com/finance/orderLedger/listData"

parameters = {"orderId": "", "originalBillId": "", "orderPlatform": "", "dataSource": "", "storeId": "", "payType": "",
              "payChannel": "", "tradeDateStart": "", "tradeDateEnd": "", "pageNo": 1, "pageSize": 10}

import csv

with open('saleDetailList.csv', 'w', newline='', encoding='utf-8') as csvfile:
    response = requests.post(url=url, json=parameters, headers=headers)
    detailList = response.json()['data']['list']
    writer = csv.DictWriter(csvfile, delimiter=r" ", fieldnames=list(detailList[0].keys()))
    writer.writeheader()
    for item in detailList:
        writer.writerow(item)
