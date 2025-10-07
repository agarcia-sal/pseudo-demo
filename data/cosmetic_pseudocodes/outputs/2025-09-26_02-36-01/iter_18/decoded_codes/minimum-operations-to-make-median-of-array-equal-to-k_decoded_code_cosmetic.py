class Solution:
    def minOperationsToMakeMedianK(self, nums, k):
        def sortAscendingOrder(arr):
            idx = 0
            n = len(arr)
            while idx < n - 1:
                inner = 0
                while inner < n - idx - 1:
                    if arr[inner] > arr[inner + 1]:
                        arr[inner], arr[inner + 1] = arr[inner + 1], arr[inner]
                    inner += 1
                idx += 1

        sortAscendingOrder(nums)
        totalCount = len(nums)
        midPos = totalCount // 2

        if nums[midPos] == k:
            return 0

        result = 0
        if nums[midPos] < k:
            checkIndex = midPos
            while checkIndex < totalCount and nums[checkIndex] < k:
                diffVal = k - nums[checkIndex]
                result += diffVal
                checkIndex += 1
        else:
            positionIndex = midPos
            while positionIndex >= 0 and nums[positionIndex] > k:
                delta = nums[positionIndex] - k
                result += delta
                positionIndex -= 1

        return result