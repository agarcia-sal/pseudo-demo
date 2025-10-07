class Solution:
    def minOperations(self, nums):
        totalCount = 0
        upperLimit = len(nums) - 2
        index = 0

        while index <= upperLimit:
            if nums[index] == 0:
                self.flipTriplet(nums, index)
                totalCount += 1
            index += 1

        if nums[-1] == 0 or nums[-2] == 0:
            return -1

        return totalCount

    def flipTriplet(self, arr, pos):
        def invert(bit):
            return 1 - bit

        arr[pos] = invert(arr[pos])
        arr[pos + 1] = invert(arr[pos + 1])
        arr[pos + 2] = invert(arr[pos + 2])