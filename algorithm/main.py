# -*- coding: utf-8 -*-
from random import Random
from algorithm.sort import qucik_sort, merge_sort

__author__ = '33504'

if __name__ == "__main__":
	arr = [Random().randint(0, 20) for x in range(20)]
	arr=[4, 4, 13, 19, 12, 8, 11, 10, 8, 18, 13, 2, 8, 20, 4, 6, 7, 16, 7, 5]
	print(arr)
	print('******************sort start******************')
	# qucik_sort = qucik_sort()
	# qucik_sort.sort(arr, 0, len(arr) - 1)
	# print(arr)

	merge_sort = merge_sort()
	merge_sort.merge(arr, 1)
	print(arr)
	print('******************sort end******************')

