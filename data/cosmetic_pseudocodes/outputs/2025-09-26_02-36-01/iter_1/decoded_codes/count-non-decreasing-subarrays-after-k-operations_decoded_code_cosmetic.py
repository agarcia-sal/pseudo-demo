class Solution:
    def countNonDecreasingSubarrays(self, nums, k):
        n = len(nums)

        def canMakeNonDecreasing(start, length):
            cost = 0
            maxVal = nums[start]
            for offset in range(1, length):
                currentVal = nums[start + offset]
                if currentVal < maxVal:
                    cost += maxVal - currentVal
                maxVal = max(maxVal, currentVal)
                if cost > k:
                    return False
            return True

        totalSubarrays = n * (n + 1) // 2
        invalidCount = 0

        for startIndex in range(n):
            low, high = 1, n - startIndex
            while low <= high:
                mid = (low + high) // 2
                if canMakeNonDecreasing(startIndex, mid):
                    low = mid + 1
                else:
                    high = mid - 1
            invalidCount += (n - startIndex - high)

        return totalSubarrays - invalidCount