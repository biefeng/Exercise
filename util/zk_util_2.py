#!usr/bin/env python
# -*- coding: utf-8 -*-
# fileName: zk_util_2.py
# time: 2020/07/16 22:48

__author__ = '33504'

from kazoo.client import KazooClient

client = KazooClient("localhost:2181")

client.start()

path = client.ensure_path("/base")
print(path)

for i in range(10):
	i_ = "/base/" + str(i) + "/"
	client.ensure_path(i_)
	for j in range(10):
		j_ = i_ + str(j) + "/"
		client.ensure_path(j_)

		for k in range(100):
			k_ = j_ + str(k) + "/"

			client.ensure_path(k_)

# def recursive_delete(path):
# 	children = client.get_children(path)
#
# 	if children is not None and len(children) > 0:
# 		for child in children:
# 			child_ = path + child + "/"
# 			sub_children = client.get_children(child_)
# 			if sub_children is not None and len(sub_children) > 0:
# 				recursive_delete(child_)
# 			else:
# 				client.delete(child_[:len(child_) - 1])
# 	client.delete(path[:len(path) - 1])
#
#
# recursive_delete("/base/")

# client.delete("/base",recursive=True)
print("finished")
client.close()

print("closed")
