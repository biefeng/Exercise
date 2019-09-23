import csv
import requests

url = "http://web.myt11.com/finance/orderLedger/listData"
headers = {
    'sid': 'f07f86912fad4e05b83cb3618fb2c225'
}
parameters = {"orderId": "", "originalBillId": "", "orderPlatform": "", "dataSource": "", "storeId": "", "payType": "",
              "payChannel": "", "tradeDateStart": "", "tradeDateEnd": "", "pageNo": 1, "pageSize": 50}

flag = True
with open("sale_detail.csv", 'w', encoding='utf-8', newline="\n") as csv_file:
    response = requests.post(url=url, headers=headers, json=parameters)
    detailList = response.json()['data']['list']
    fields = list(detailList[0].keys())
    fields.append('orderSource')
    fields.append("refundTypeStr")
    fields.append("refundType")
    fields.append("remark")
    writer = csv.DictWriter(csv_file, fieldnames=fields, delimiter=r" ")
    writer.writeheader()
    while flag == True:
        response = requests.post(url=url, headers=headers, json=parameters)
        detailList = response.json()['data']['list']
        if len(detailList) > 0 and parameters['pageNo'] <= 2000:
            for row in detailList:
                writer.writerow(row)
            parameters['pageNo'] = parameters['pageNo'] + 1
            print("-------------fetch date ,pageNO: " + str(parameters["pageNo"]))
        else:
            flag = False
