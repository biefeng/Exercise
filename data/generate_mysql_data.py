# -*- coding: utf-8 -*-
__author__ = '33504'

# coding=utf-8
from faker import Factory
import uniout
import logging
import threading
import random
import time
from datetime import datetime
from orator import DatabaseManager, Model

print
"开始..."
fake = Factory.create('zh_CN')

# 创建 日志 对象
logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter(
	'%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

# Connect to the database

config = {
	'mysql': {
		'driver': 'mysql',
		'host': '192.168.186.137',
		'database': 'test',
		'user': 'root',
		'password': 'Biefeng123!',
		'prefix': ''
	}
}

db = DatabaseManager(config)
Model.set_connection_resolver(db)


class User(Model):
	__table__ = 'user'
	pass


thread_nums = 10
ARR = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
LAST = ('1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2')


def makeIdNo():
	u''' 随机生成新的18为身份证号码 '''
	t = time.localtime()[0]
	x = '%02d%02d%02d%04d%02d%02d%03d' % (random.randint(10, 99),
	                                      random.randint(1, 99),
	                                      random.randint(1, 99),
	                                      random.randint(t - 80, t - 18),
	                                      random.randint(1, 12),
	                                      random.randint(1, 28),
	                                      random.randint(1, 999))
	y = 0
	for i in range(17):
		y += int(x[i]) * ARR[i]

	return '%s%s' % (x, LAST[y % 11])


def insert_user(thread_name, nums):
	logger.info('开启线程%s' % thread_name)
	for _ in range(nums):
		email = fake.email()
		job = fake.job()
		address = fake.address().encode('utf-8')
		password = fake.md5()
		text = fake.text().encode('utf-8')
		username = str(fake.user_name())
		truename = fake.name().encode('utf-8')
		create_time = fake.date_time_between_dates(
			datetime_start=datetime(2017, 1, 1, 0, 0, 0),
			datetime_end=datetime(2017, 8, 12, 0, 0, 0, 0))
		create_time = str(create_time)
		company = fake.company().encode('utf-8')
		# Create a new record
		user = User()
		user.tel = fake.phone_number()
		user.username = username
		user.truename = truename
		user.job = job
		user.company = company
		user.password = password
		user.email = email
		user.id_no = makeIdNo()
		user.city_id = random.randint(1, 290)
		user.address = address
		user.summary = text
		user.gender = random.randint(1, 2)
		user.age = fake.random_int(10, 50)
		user.site = fake.uri()
		user.uuid = fake.uuid4()
		user.save()


for i in range(thread_nums):
	t = threading.Thread(target=insert_user, args=(i, 600000))
	t.start()