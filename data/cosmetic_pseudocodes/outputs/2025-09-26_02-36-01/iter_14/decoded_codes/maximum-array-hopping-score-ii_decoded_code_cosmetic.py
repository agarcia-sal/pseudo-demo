from typing import List

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        k = len(nums)
        cache = [0] * k
        a = k - 2
        while a >= 0:
            highest = 0
            b = a + 1
            while b <= k - 1:
                current_score = (b - a) * nums[b]
                if highest < current_score + cache[b]:
                    highest = current_score + cache[b]
                b += 1
            cache[a] = highest
            a -= 1
        return cache[0]