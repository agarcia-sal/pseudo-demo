class Solution:
    def minOperationsToMakeMedianK(self, nums, k):
        def HeapSort(arr):
            def SiftDown(start, end):
                root = start
                while True:
                    child = 2 * root + 1
                    if child > end:
                        return
                    if child + 1 <= end and arr[child] < arr[child + 1]:
                        child += 1
                    if arr[root] < arr[child]:
                        arr[root], arr[child] = arr[child], arr[root]
                        root = child
                    else:
                        return

            size = len(arr)
            i = (size // 2) - 1
            while i >= 0:
                SiftDown(i, size - 1)
                i -= 1
            j = size - 1
            while j > 0:
                arr[0], arr[j] = arr[j], arr[0]
                SiftDown(0, j - 1)
                j -= 1

        HeapSort(nums)
        total_length = len(nums)
        mid_pos = total_length // 2

        if nums[mid_pos] == k:
            return 0

        def IncreaseWhileLessThanK(idx):
            if idx >= total_length or nums[idx] >= k:
                return 0
            diff = k - nums[idx]
            return diff + IncreaseWhileLessThanK(idx + 1)

        def DecreaseWhileGreaterThanK(idx):
            if idx < 0 or nums[idx] <= k:
                return 0
            diff = nums[idx] - k
            return diff + DecreaseWhileGreaterThanK(idx - 1)

        if nums[mid_pos] < k:
            total_ops = IncreaseWhileLessThanK(mid_pos)
        else:
            total_ops = DecreaseWhileGreaterThanK(mid_pos)

        return total_ops