from random import Random


class qucik_sort:
	def find_middle(self, arr, start, end):
		pass

	def sort(self, arr, start, end):
		left = start
		right = end
		if left >= right:
			return
		key = arr[left]

		while right > left:
			while arr[right] >= key and right > left:
				right = right - 1
			else:
				arr[left] = arr[right]

			while arr[left] < key and right > left:
				left = left + 1
			else:
				arr[right] = arr[left]

			arr[right] = arr[left]

		arr[left] = key

		self.sort(arr, start, left)
		self.sort(arr, left + 1, end)


class merge_sort:
	pass

	def merge(self, arr, p):
		rec = arr[0:len(arr)]
		group = int((len(arr) + 1) / (1 << p))
		if group <= 0:
			return

		for x in range(group):
			start = (1 << p) * x
			end = (1 << p) * (x + 1)
			if x == group - 1:
				end = len(arr)
			start_1 = 0
			start_2 = 1 << (p - 1)
			tmp = arr[start:end]
			for (y, item) in enumerate(tmp):
				if start_2 <= len(tmp) - 1 :
					if start_1 >= 1 << (p - 1):
						arr[start + y] = tmp[start_2]
						start_2 = start_2 + 1
						continue

					if tmp[start_2] > tmp[start_1]:
						arr[start + y] = tmp[start_1]
						start_1 = start_1 + 1
					else:
						arr[start + y] = tmp[start_2]
						start_2 = start_2 + 1
				else:
					arr[start + y] = tmp[start_1]
					start_1 = start_1 + 1
		self.merge(arr, p + 1)

	def sort(self, arr, start, end):
		pass
