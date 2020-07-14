#!/usr/bin/env python
# -*- coding:utf-8 -*-
# filename: b_plus_tree.py
# py version: 3.6


class InternalNode:
    def __init__(self, key):
        self.key = key


class LeafNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class BPlsuTree:
    def __init__(self, m):
        self.m = m
