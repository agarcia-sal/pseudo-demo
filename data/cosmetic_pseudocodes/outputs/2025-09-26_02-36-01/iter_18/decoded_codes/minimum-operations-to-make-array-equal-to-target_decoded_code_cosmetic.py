class Solution:
    def minimumOperations(self, nums, target):
        u = len(nums)
        v = abs(target[0] - nums[0])
        w = 1
        while w < u:
            p = target[w] - nums[w]
            q = target[w - 1] - nums[w - 1]
            if p * q > 0:
                r = abs(p) - abs(q)
                if r > 0:
                    v += r
            else:
                v += abs(p)
            w += 1
        return v