class Solution:
    def minOperations(self, nums):
        m = 0
        n = 0
        p = 0
        q = len(nums)
        while p < q:
            if not (n % 2 == 1):
                r = nums[p]
            else:
                r = 1 - nums[p]
            if r == 0:
                m += 1
                n += 1
            p += 1
        return m