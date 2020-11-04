import csv
import requests

url = "http://web.myt11.com/finance/orderLedger/listData"
headers = {
    "app": "nosession"
}
parameters = {"orderId": "", "originalBillId": "", "orderPlatform": "", "dataSource": "", "storeId": '',
              "payType": "", "payChannel": "", "reconStatus": "", "tradeDateStart": "2020-10-28",
              "tradeDateEnd": "2020-11-04", "pageNo": 1, "pageSize": 30}

flag = True
with open("sale_detail_11_04.csv", 'w', encoding='utf-8', newline="\n") as csv_file:
    response = requests.post(url=url, headers=headers, json=parameters)
    # print(response.content)
    detailList = response.json()['data']['list']
    fields = set(detailList[0].keys())
    fields.add('orderSource')
    fields.add("refundTypeStr")
    fields.add("refundType")
    fields.add("remark")
    fields.add("accountSn")
    fields.add("thirdPartChannelStr")
    fields.add("thirdPartChannel")
    fields.add("thirdPartPayChannel")
    fields.add("bankCode")
    fields.add("orderTypeStr")
    fields.add("orderType")
    writer = csv.DictWriter(csv_file, fieldnames=list(fields), delimiter=r" ")
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
    print("Fetch finished")
