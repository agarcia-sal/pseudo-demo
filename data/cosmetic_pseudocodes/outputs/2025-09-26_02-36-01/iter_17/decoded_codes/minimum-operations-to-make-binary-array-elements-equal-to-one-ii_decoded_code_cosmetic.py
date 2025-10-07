class Solution:
    def minOperations(self, nums):
        totalOps = 0
        toggleFlag = 0
        index = 0
        n = len(nums)
        while index < n:
            modResult = toggleFlag % 2
            valAtIndex = nums[index] if modResult == 0 else 1 - nums[index]
            if valAtIndex == 0:
                totalOps += 1
                toggleFlag += 1
            index += 1
        return totalOps