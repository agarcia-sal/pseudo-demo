class Solution:
    def maximumLength(self, nums, k):
        totalElements = len(nums)
        if totalElements == 1:
            return 1

        dpArray = [{} for _ in range(totalElements)]
        longestChain = 1

        for idxOuter in range(totalElements):
            for idxInner in range(idxOuter):
                currentSum = nums[idxOuter] + nums[idxInner]
                modValue = currentSum % k
                if modValue in dpArray[idxInner]:
                    dpArray[idxOuter][modValue] = dpArray[idxInner][modValue] + 1
                else:
                    dpArray[idxOuter][modValue] = 2

                if dpArray[idxOuter][modValue] > longestChain:
                    longestChain = dpArray[idxOuter][modValue]

        return longestChain