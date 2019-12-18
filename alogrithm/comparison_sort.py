#!/usr/bin/env python
# -*- coding:utf-8 -*-
# filename: comparison_sort.py
# py version: 3.6


class InsertSort:
    @staticmethod
    def sort(arr=[]):
        for i in range(len(arr)):
            for j in range(i + 1):
                if arr[i] > arr[j]:
                    tmp = arr[j]
                    arr[j] = arr[i]
                    arr[i] = tmp


class MergeSort:

    def sort(self, arr=[]):
        return self.__sort_internal(arr)

    def __sort_internal(self, arr=[]):
        mid = int(len(arr) / 2)
        if len(arr) <= 1:
            return arr
        arr_l = self.__sort_internal(arr[:mid])
        arr_r = self.__sort_internal(arr[mid:])
        return self.__merge_sort(arr_l, arr_r)

    @staticmethod
    def __merge_sort(left, right):
        """将已有序的左右两段进行合并"""
        index_l = 0
        index_r = 0
        result = []
        while index_l < len(left) and index_r < len(right):
            if left[index_l] > right[index_r]:
                result.append(right[index_r])
                index_r = index_r + 1
            else:
                result.append(left[index_l])
                index_l = index_l + 1
        result += left[index_l:]
        result += right[index_r:]
        return result


class QuickSort:
    pass


from random import Random

if __name__ == '__main__':
    r = Random(8)
    arr = [r.randint(0, 100) for i in range(100)]
    print(arr)
    mergeSort = MergeSort()
    mergeSort.sort(arr)
    print(mergeSort.sort(arr))
