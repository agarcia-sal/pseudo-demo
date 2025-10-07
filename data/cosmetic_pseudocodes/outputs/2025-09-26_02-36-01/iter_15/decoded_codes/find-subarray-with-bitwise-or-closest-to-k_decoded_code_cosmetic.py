from math import inf

class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        a = len(nums)
        d = inf

        x = 0
        while x <= a - 1:
            y = x
            m = 0
            while y <= a - 1:
                m |= nums[y]
                s = abs(k - m)
                if s < d:
                    d = s
                if s == 0:
                    return 0
                y += 1
            x += 1

        return d