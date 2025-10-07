class Solution:
    def minOperationsToMakeMedianK(self, nums, k):
        def sortListAscending(arr):
            i = 0
            lengthArr = len(arr)
            while i < lengthArr - 1:
                j = i + 1
                while j < lengthArr:
                    if arr[i] > arr[j]:
                        arr[i], arr[j] = arr[j], arr[i]
                    j += 1
                i += 1

        sortListAscending(nums)
        sizeCount = len(nums)
        medPos = sizeCount // 2  # median index

        if not (nums[medPos] != k):
            return 0

        if nums[medPos] < k:
            medCur = medPos

            def increaseOps(currentMedian, accumOps):
                if currentMedian >= sizeCount:
                    return accumOps
                if nums[currentMedian] >= k:
                    return accumOps
                diffVal = k - nums[currentMedian]
                return increaseOps(currentMedian + 1, accumOps + diffVal)

            changeCount = increaseOps(medCur, 0)

        else:
            medCur = medPos

            def decreaseOps(currentMedian, accumOps):
                if currentMedian < 0:
                    return accumOps
                if nums[currentMedian] <= k:
                    return accumOps
                diffVal = nums[currentMedian] - k
                return decreaseOps(currentMedian - 1, accumOps + diffVal)

            changeCount = decreaseOps(medCur, 0)

        return changeCount