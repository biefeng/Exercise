#!usr/bin/env python
# -*- coding: utf-8 -*-
# fileName: btree.py
# time: 2019/09/23 23:22

__author__ = '33504'


class BTreeNode:
	def __init__(self, m, parent):
		self.__m = m
		self.__values = [] * 10
		self.__parent = parent

	def exceed(self):
		if len(self.__values) > self.__m:
			return True
		return False
	def