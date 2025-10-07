class Solution:
    def minimumOperations(self, nums, target):
        m = 0
        p = len(nums)
        m = abs(target[0] - nums[0])
        q = 1
        while q < p:
            r = target[q] - nums[q]
            s = target[q - 1] - nums[q - 1]
            if r * s > 0:
                t = abs(r) - abs(s)
                if t > 0:
                    m += t
            else:
                m += abs(r)
            q += 1
        return m