class Solution:
    def maximumSubarraySum(self, nums, k):
        prefixSumsMap = {}
        maxVal = (-1) * (2 ** 63) - 1
        prefixTotal = 0
        index = 0

        while index < len(nums):
            val = nums[index]
            targetMinus = val - k
            if targetMinus in prefixSumsMap:
                candidate = prefixTotal - prefixSumsMap[targetMinus] + val
                if candidate > maxVal:
                    maxVal = candidate

            targetPlus = val + k
            if targetPlus in prefixSumsMap:
                candidateAlt = prefixTotal - prefixSumsMap[targetPlus] + val
                if candidateAlt > maxVal:
                    maxVal = candidateAlt

            if val in prefixSumsMap:
                if prefixSumsMap[val] > prefixTotal:
                    prefixSumsMap[val] = prefixTotal
            else:
                prefixSumsMap[val] = prefixTotal

            prefixTotal += val
            index += 1

        if maxVal != (-1) * (2 ** 63) - 1:
            return maxVal
        else:
            return 0