# -*- coding: utf-8 -*-
# py version 3.6

__author__ = '33504'


class Node:
	def __init__(self, root, key, value):
		self.parent = None
		self.key = key
		self.value = value

	def set_parent(self, parent):
		self.parent = parent


class BTree:

	def __init__(self, m):
		self.m = m
		self.root = None
		pass

	def insert(self, key, value):
		node = Node(key, value)
		if self.root == None:
			self.root = node
		pass
