# -*- coding: utf-8 -*-
__author__ = '33504'

import logging

import pymysql.cursors
from faker import Factory

fake = Factory.create('zh_CN')

# 创建 日志 对象
logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter(
	'%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)


def insert_data(table):
	fake = Factory.create('zh_CN')
	connection = pymysql.connect(host='192.168.186.137',
	                             user='root',
	                             password='root',
	                             db='test',
	                             charset='utf8mb4',
	                             cursorclass=pymysql.cursors.DictCursor)

	try:
		with connection.cursor()as cursor:

			for index in range(10):
				order_no =fake.address()
				sql = "insert into order_head (order_no,order_time,user_id,address,amount,source,status) value ()"
				cursor.execute(sql)
			cursor.commit()
	finally:
		connection.close()
