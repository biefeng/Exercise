# -*- coding:utf-8 -*-
# author : BieFeNg
# date_time 2019/12/17 17:05
# file_name : fetch_order_detail.py
import csv
import requests
import pymysql
from datetime import date, datetime, timedelta

page_size = 10

start_time = datetime(2019, 6, 5, 0, 0, 0)
end_time = datetime(2019, 6, 5, 23, 59, 59)

final_end_time = datetime(2019, 12, 18, 23, 59, 59)

interval = timedelta(1)

diff_date = (final_end_time - end_time).days

order_url = "http://web.myt11.com/oms/order/findByPage"
detail_url_prefix = "http://web.myt11.com/oms/order/findOrderDetail?"

# headers
headers = {
    'sid': 'fc249685a53a424e941db1040d5c061d'
}

order_params = {"orderQueryDto": {"orderId": "", "receiver": "", "startTime": "2019-11-17 00:00:00",
                                  "endTime": "2019-12-17 23:59:59", "sendPay": "", "thanPrice": "", "storeId": "",
                                  "userId": "", "orderSource": "", "paymentWayId": "", "lessPrice": "", "state": "100",
                                  "mobile": "", "sku": ""}, "pageHelper": {"page": 1, "rows": page_size}}

detail_params = {"orderId": "2120013300000065832",
                 "userMobile": "13466665886"}

connection = pymysql.connect(host="192.168.186.135", user="root", password="Biefeng123!",
                             database="recosys")
cursor = connection.cursor(cursor=pymysql.cursors.DictCursor)


def handle_order_list(order_lsit, cursor, writer):
    for order in order_lsit:
        detail_params['orderId'] = order['orderId']
        detail_url = detail_url_prefix + "orderId=" + str(order['orderId'])
        if "mobile" in order:
            detail_url = detail_url + "&userMobile=" + str(order['mobile'])
        detail_response = requests.get(url=detail_url, headers=headers)
        order_items = detail_response.json()['data']['orderDataDetail']['orderItems']
        for order_item in order_items:
            sql = "insert into order_detail (sku_id,order_id,user_id,order_time,sku_name) values (" + "'" + str(
                order_item['skuId']) + "'," + "'" + str(
                order['orderId']) + "'," + "'" + str(
                order['userId']) + "'," + "'" + str(
                order['orderCreateDate']) + "'," + "'" + str(order_item['productName']) + "');"
            try:
                cursor.execute(sql)
                connection.commit()
            except Exception as e:
                connection.rollback()
                print(sql)


with open("order_detail.csv", 'w', encoding='utf-8', newline="\n") as csv_file:
    fields = ['sku_id', 'sku_name', 'order_id', 'order_time', 'user_id']
    writer = csv.DictWriter(csv_file, fieldnames=fields, delimiter=r" ")
    writer.writeheader()
    for day_ in range(diff_date):
        start_time = start_time + interval
        end_time = end_time + interval
        order_params['orderQueryDto']['startTime'] = str(start_time)
        order_params['orderQueryDto']['endTime'] = str(end_time)
        response = requests.post(url=order_url, headers=headers, json=order_params)
        response_data = response.json()['data']
        count = response_data['count']
        order_lsit = response_data['list']
        handle_order_list(order_lsit, cursor, writer)
        page_count = (count + page_size - 1) // page_size
        print("****订单时间：" + str(start_time) + "-" + str(end_time) + ", 订单数量：" + str(count) + "****")
        for page_no in range(page_count):
            if page_no > 0:
                order_params['pageHelper']['page'] = page_no + 1
                response = requests.post(url=order_url, headers=headers, json=order_params)
                response_data = response.json()['data']
                count = response_data['count']
                order_lsit = response_data['list']
                handle_order_list(order_lsit, cursor, writer)

#
# flag = True

#
#

#
#
# with open("order_detail.csv", 'w', encoding='utf-8', newline="\n") as csv_file:
#     response = requests.post(url=order_url, headers=headers, json=order_params)
#     order_lsit = response.json()['data']['list']
#     for order in order_lsit:
#         detail_params['orderId'] = order['orderId']
#         detail_url = detail_url_prefix + "orderId=" + str(order['orderId'])
#         if "mobile" in order:
#             detail_url = detail_url + "&userMobile=" + str(order['mobile'])
#         detail_response = requests.get(url=detail_url, headers=headers)
#         order_items = detail_response.json()['data']['orderDataDetail']['orderItems']
#         for order_item in order_items:
#             sql = "insert into order_detail (sku_id,order_id,sku_name) values (" + "'" + str(
#                 order_item['skuId']) + "'," + "'" + str(
#                 order['orderId']) + "'," + "'" + str(order_item['productName']) + "');"
#             print(sql)
#             cursor.execute(sql)
#             connection.commit()

# fields = list(detailList[0].keys())
# fields.append('orderSource')
# fields.append("refundTypeStr")
# fields.append("refundType")
# fields.append("remark")
# writer = csv.DictWriter(csv_file, fieldnames=fields, delimiter=r" ")
# writer.writeheader()
# while flag:
#     response = requests.post(url=url, headers=headers, json=parameters)
#     detailList = response.json()['data']['list']
#     if len(detailList) > 0 and parameters['pageNo'] <= 2000:
#         for row in detailList:
#             writer.writerow(row)
#         parameters['pageNo'] = parameters['pageNo'] + 1
#         print("-------------fetch date ,pageNO: " + str(parameters["pageNo"]))
#     else:
#         flag = False
