class Solution:
    def minimumOperations(self, nums: list[int], target: list[int]) -> int:
        p = abs(target[0] - nums[0])
        q = len(nums)
        r = 1
        while r < q:
            m = target[r] - nums[r]
            s = target[r - 1] - nums[r - 1]
            if m * s > 0:
                u = abs(m)
                v = abs(s)
                w = u - v
                if w > 0:
                    p += w
            else:
                p += abs(m)
            r += 1
        return p