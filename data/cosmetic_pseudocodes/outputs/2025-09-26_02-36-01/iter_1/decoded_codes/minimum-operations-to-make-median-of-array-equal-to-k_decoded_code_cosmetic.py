class Solution:
    def minOperationsToMakeMedianK(self, nums, k):
        sortedNums = sorted(nums)
        length = len(sortedNums)
        mid = length // 2

        if sortedNums[mid] == k:
            return 0

        totalOps = 0

        if sortedNums[mid] < k:
            while mid < length and sortedNums[mid] < k:
                totalOps += k - sortedNums[mid]
                mid += 1
        else:
            while mid >= 0 and sortedNums[mid] > k:
                totalOps += sortedNums[mid] - k
                mid -= 1

        return totalOps