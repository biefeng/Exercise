import requests

url = "http://172.16.1.184:80/catering/sku/listData"

payload = "{\"skuId\":\"\",\"opt\":\"\",\"isAuthSql\":0,\"pageNo\":1,\"pageSize\":10,\"shopId\":12001}"
headers = {
    'sid': "7c4215eeed194d8cb0a2e57e11bb9231",
    'app': "nosession",
    'shopId': "12001",
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "20d4af79-b8a4-493f-acfe-bef20640214d"
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.json())
