class Solution:
    def maxSubarraySum(self, nums):
        def kadane(arr):
            def internalKadane(index, currentMax, globalMax):
                if index > len(arr) - 1:
                    return globalMax
                candidate1 = arr[index]
                candidate2 = currentMax + arr[index]
                newCurrentMax = candidate1 if candidate1 > candidate2 else candidate2
                newGlobalMax = newCurrentMax if globalMax < newCurrentMax else globalMax
                return internalKadane(index + 1, newCurrentMax, newGlobalMax)

            return internalKadane(1, arr[0], arr[0])

        intermediateMaxSum = kadane(nums)
        uniqueSet = set()
        i = 0
        while i < len(nums):
            uniqueSet.add(nums[i])
            i += 1

        iterator = 0
        keyList = list(uniqueSet)
        while iterator < len(keyList):
            excludeValue = keyList[iterator]
            filteredNums = []
            j = 0
            while j < len(nums):
                if nums[j] != excludeValue:
                    filteredNums.append(nums[j])
                j += 1

            if len(filteredNums) > 0:
                tempMax = kadane(filteredNums)
                if intermediateMaxSum < tempMax:
                    intermediateMaxSum = tempMax
            iterator += 1

        return intermediateMaxSum