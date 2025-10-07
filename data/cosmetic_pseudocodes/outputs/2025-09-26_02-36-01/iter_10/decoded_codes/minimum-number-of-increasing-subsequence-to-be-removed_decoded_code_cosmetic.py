class Solution:
    def minOperations(self, nums):
        def getMax(arr):
            res = arr[0]
            idx = 1
            while idx < len(arr):
                if arr[idx] > res:
                    res = arr[idx]
                idx += 1
            return res

        totalElements = len(nums)
        if totalElements == 0:
            return 0

        def buildDp(lst, size):
            def recurse(pos, dpList):
                if pos >= size:
                    return dpList

                def innerLoop(innerPos, updatedDp):
                    if innerPos < 0:
                        return updatedDp
                    if lst[pos] <= lst[innerPos]:
                        if updatedDp[pos] < updatedDp[innerPos] + 1:
                            updatedDp[pos] = updatedDp[innerPos] + 1
                    return innerLoop(innerPos - 1, updatedDp)

                currentDp = innerLoop(pos - 1, dpList)
                return recurse(pos + 1, currentDp)

            return recurse(1, [1 for _ in range(size)])

        dpValues = buildDp(nums, totalElements)
        return getMax(dpValues)