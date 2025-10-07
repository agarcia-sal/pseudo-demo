from typing import List

class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        l = len(nums)
        s = [0] * (k + 3)  # +3 to safely handle indices up to MAX + 2
        r = 0
        half = l // 2

        while r < half:
            a = nums[r]
            b = nums[l - r - 1]

            if a < b:
                a, b = b, a

            s[0] += 1
            s[b - a] -= 1
            s[b - a + 1] += 1
            idx = max(b, k - a) + 1
            s[idx] -= 1
            s[idx + 1] += 2

            r += 1

        u = s[0]
        v = u
        for t in range(k + 1):
            u += s[t + 1]
            if u < v:
                v = u

        return v