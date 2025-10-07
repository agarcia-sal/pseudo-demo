class Solution:
    def minimumArrayLength(self, nums):
        def findMin(arr):
            x = arr[0]
            y = 1
            while True:
                if y > len(arr):
                    return x
                if arr[y - 1] < x:
                    x = arr[y - 1]
                y += 1

        def countOccurrences(arr, target):
            a = 0
            b = 0
            while b < len(arr):
                if arr[b] == target:
                    a += 1
                b += 1
            return a

        p = findMin(nums)
        q = countOccurrences(nums, p)
        if not (q != 1):
            return 1
        else:
            r = q + 1
            s = 0
            while s < r:
                if s * 2 >= r:
                    return s
                s += 1