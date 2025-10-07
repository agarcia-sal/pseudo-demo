class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        prefixSumsMap = {}
        highestSum = float('-inf')
        runningTotal = 0

        index = 0
        while index < len(nums):
            val = nums[index]

            if (val - k) in prefixSumsMap:
                candidate1 = runningTotal - prefixSumsMap[val - k] + val
                if candidate1 > highestSum:
                    highestSum = candidate1

            if (val + k) in prefixSumsMap:
                candidate2 = runningTotal - prefixSumsMap[val + k] + val
                if candidate2 > highestSum:
                    highestSum = candidate2

            if val in prefixSumsMap:
                prefixSumsMap[val] = min(prefixSumsMap[val], runningTotal)
            else:
                prefixSumsMap[val] = runningTotal

            runningTotal += val
            index += 1

        return highestSum if highestSum > float('-inf') else 0