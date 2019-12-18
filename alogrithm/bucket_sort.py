#!/usr/bin/env python
# -*- coding:utf-8 -*-
# filename: bucket_sort.py
# py version: 3.6


def bin_sort(li, min_num, max_num, bin_num=10):
    bin = [[] for i in range(bin_num)]  # [ [],[],[],...  ]
    for num in li:
        n = (max_num - min_num + 1) / bin_num  # 表示多少个数在一个桶里
        bin[int(num // n)].append(num)  # 对应的数字放在对应的桶里

        # 维护桶有序，每一个桶使用插入排序，注意这是对每一个桶中的数进行排序
        i = len(bin[int(num // n)]) - 1  # i表示桶中的最后一个数
        tmp = bin[int(num // n)][i]
        j = i - 1
        while j >= 0 and tmp < bin[int(num // n)][j]:
            bin[int(num // n)][j + 1] = bin[int(num // n)][j]
            j = j - 1
        bin[int(num // n)][j + 1] = tmp
    # 对每一个桶中的数进行合并，返回已经排序好的序列
    res = []
    for l in bin:
        res.extend(l)
    return res


import random

li = [random.randint(0, 600) for i in range(10000)]
print(bin_sort(li, 0, 600))
