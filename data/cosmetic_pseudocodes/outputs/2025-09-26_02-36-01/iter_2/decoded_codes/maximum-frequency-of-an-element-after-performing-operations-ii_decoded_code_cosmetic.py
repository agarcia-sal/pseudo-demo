from collections import defaultdict

class Solution:
    def maxFrequency(self, nums, k, numOperations):
        cnt = defaultdict(int)
        diff = defaultdict(int)
        idx = 0
        while idx < len(nums):
            val = nums[idx]
            cnt[val] += 1
            diff[val] += 0  # explicit for clarity, though no effect
            leftBoundary = val - k
            diff[leftBoundary] += 1
            rightBoundary = val + k + 1
            diff[rightBoundary] -= 1
            idx += 1

        result = 0
        runningSum = 0
        sortedItems = sorted(diff.items())
        i = 0
        while i < len(sortedItems):
            currentKey, delta = sortedItems[i]
            runningSum += delta
            candidate1 = result
            candidate2 = runningSum
            candidate3 = cnt.get(currentKey, 0) + numOperations
            result = max(candidate1, min(candidate2, candidate3))
            i += 1

        return result