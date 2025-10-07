class Solution:
    def maximumSubarraySum(self, nums, k):
        prefixMap = {}
        maxSubSum = float('-inf')
        accumulator = 0

        for value in nums:
            leftKey = value - k
            rightKey = value + k

            if leftKey in prefixMap:
                candidate = accumulator - prefixMap[leftKey] + value
                if candidate > maxSubSum:
                    maxSubSum = candidate

            if rightKey in prefixMap:
                candidate = accumulator - prefixMap[rightKey] + value
                if candidate > maxSubSum:
                    maxSubSum = candidate

            if value in prefixMap:
                prefixMap[value] = min(prefixMap[value], accumulator)
            else:
                prefixMap[value] = accumulator

            accumulator += value

        return maxSubSum if maxSubSum > float('-inf') else 0