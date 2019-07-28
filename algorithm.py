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


if __name__ == "__main__":
    arr = [Random().randint(0, 100) for x in range(50)]

    qucik_sort = qucik_sort()
    qucik_sort.sort(arr, 0, len(arr) - 1)
    print('************************************')
    print(arr)


class merge_sort:
    pass

    def merge(self, arr, p):
        group = len(arr) + 1 - 1 << p
        for x in range(group):
            start = (1 << p) * x
            end = (1 << p) * (x + 1)
            if x == group - 1:
                end = len(arr)
            start_1 = 1 << (p - 1)
            tmp = arr[start:end]
            for (y, item) in enumerate(tmp):
                if arr[start_1]:
                    if arr[start_1] > arr[start]:
                        arr[y] = item
                    else:

                        arr[y] = item
                else:
                    arr[y] = item

    def sort(self, arr, start, end):
        pass
