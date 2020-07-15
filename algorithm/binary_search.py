# -*- coding: utf-8 -*-
__author__ = '33504'


def binary_search(arr, e):
	if arr is None or not isinstance(arr, list):
		raise RuntimeError("arr can not be None and must be a list")

	lo = 0
	hi = len(arr)
	while lo < hi:
		mid = int((hi + lo) / 2)
		if e < arr[mid]:
			hi = mid
		elif e > arr[mid]:
			lo = mid
		else:
			return mid
	return -1


search = binary_search([2, 3, 4, 5, 6, 7, 8, 9], 1)
print(search)
