class Solution:
    def minOperations(self, nums):
        delta = len(nums)
        omega = 0
        psi = 0
        while psi < delta - 2:
            if nums[psi] == 0:
                self.flipBit(nums, psi)
                self.flipBit(nums, psi + 1)
                self.flipBit(nums, psi + 2)
                omega += 1
            psi += 1

        if self.zeroCheck(nums[delta - 1]) or self.zeroCheck(nums[delta - 2]):
            return -1

        return omega

    def flipBit(self, arr, pos):
        arr[pos] = 1 - arr[pos]

    def zeroCheck(self, val):
        return val == 0