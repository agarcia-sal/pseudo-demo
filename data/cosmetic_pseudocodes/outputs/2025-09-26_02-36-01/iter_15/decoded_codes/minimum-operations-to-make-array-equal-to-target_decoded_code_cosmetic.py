class Solution:
    def minimumOperations(self, nums, target):
        a = len(nums)
        b = abs(target[0] - nums[0])
        c = 1
        while c < a:
            p = target[c] - nums[c]
            q = target[c - 1] - nums[c - 1]
            if not (p * q <= 0):
                r = abs(abs(p) - abs(q))
                if r > 0:
                    b += r
            else:
                b += abs(p)
            c += 1
        return b