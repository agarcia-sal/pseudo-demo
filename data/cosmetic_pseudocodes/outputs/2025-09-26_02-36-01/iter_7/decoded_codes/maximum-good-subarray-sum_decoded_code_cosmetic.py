class Solution:
    def maximumSubarraySum(self, nums, k):
        NEG_INF = - (1 << 31) - (1 << 30)  # large negative number
        prefixMap = {}
        totalAccum = 0
        bestVal = NEG_INF

        def checkAndUpdate(targetKey):
            nonlocal bestVal, totalAccum
            if targetKey in prefixMap:
                candidate = totalAccum - prefixMap[targetKey] + targetKey
                if candidate > bestVal:
                    bestVal = candidate

        idx = 0
        n = len(nums)
        while idx < n:
            element = nums[idx]
            checkAndUpdate(element - k)
            checkAndUpdate(element + k)

            if element in prefixMap:
                oldVal = prefixMap[element]
                if totalAccum < oldVal:
                    prefixMap[element] = totalAccum
            else:
                prefixMap[element] = totalAccum

            totalAccum += element
            idx += 1

        return bestVal if bestVal != NEG_INF else 0