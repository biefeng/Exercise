#!/usr/bin/env python
# -*- coding:utf-8 -*-
# filename: b_tree.py
# py version: 3

from math import ceil
from random import Random


class BTreeNode:
    def __init__(self, m, p):
        self.__m = m
        self.__key = None
        self.__elements = [] * m
        self.__children = []
        self.__parent = p

    def expand(self):
        if len(self.__elements) >= self.__m:
            return True
        return False

    def shrink(self):
        if len(self.__elements) <= ceil(self.__m / 2):
            return True
        return False

    def insert(self, value):
        self.insertSort(self.__elements, value)
        if self.expand():
            self.split()

    def split(self):
        len = len(self.__elements)
        mid = len // 2
        value = self.__elements[mid]
        self.__parent.insert(value)
        self.__elements.remove(mid)
        pass

    def insertSort(self, arr, value):
        arr.append(value)
        for i in range(len(arr)):
            for j in range(i + 1):
                if arr[j] > arr[i]:
                    tmp = arr[j]
                    arr[j] = arr[i]
                    arr[i] = tmp


class BTree(object):
    def __init__(self, m=3):
        self.__m = m
        self.__root = None

    def insert(self, value):
        if self.__root is None:
            node = BTreeNode(self.__m, None)
            node.__key = value
            node.append_val(value)
            self.__root = node
        else:
            self.__root.append_val(value)

    def compare(self, arr, value):
        for e in arr:
            pass


if __name__ == '__main__':
    r = Random()
    l = []
    for i in range(10):
        l.append(r.randint(0, 20))

    node = BTreeNode(3, None)
    node.insertSort(l, 22)
