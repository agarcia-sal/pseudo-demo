class Solution:
    def minOperationsToMakeMedianK(self, nums, k):
        def helperSort(lst):
            idxA = 0
            idxB = len(lst) - 1
            while True:
                swapped = False
                for tempX in range(idxA, idxB):
                    if lst[tempX] > lst[tempX + 1]:
                        lst[tempX], lst[tempX + 1] = lst[tempX + 1], lst[tempX]
                        swapped = True
                idxB -= 1
                if not swapped:
                    break

        helperSort(nums)

        lenVal = len(nums)
        midPos = lenVal // 2

        if nums[midPos] == k:
            return 0

        resultCount = 0

        if nums[midPos] < k:
            def climbUp(i, accum):
                if i >= lenVal:
                    return accum
                if nums[i] >= k:
                    return accum
                delta = k - nums[i]
                return climbUp(i + 1, accum + delta)
            resultCount = climbUp(midPos, 0)
        else:
            def climbDown(j, accum):
                if j < 0:
                    return accum
                if nums[j] <= k:
                    return accum
                diff = nums[j] - k
                return climbDown(j - 1, accum + diff)
            resultCount = climbDown(midPos, 0)

        return resultCount