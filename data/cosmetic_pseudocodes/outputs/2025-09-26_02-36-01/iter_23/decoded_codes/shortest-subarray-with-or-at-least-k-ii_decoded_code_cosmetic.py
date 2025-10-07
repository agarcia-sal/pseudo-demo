from math import inf
from typing import List

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        def f642(m17: List[int], v12: int):
            x07 = 1
            for j19 in range(32):
                if (m17[j19] & x07) != 0:
                    m17[j19] += v12
                x07 <<= 1

        def w89(a28: List[int]) -> int:
            p29 = 0
            for k12 in range(32):
                if a28[k12] > 0:
                    p29 |= (1 << k12)
            return p29

        v97 = len(nums)
        s68 = [0] * 32
        b54 = 0
        u15 = 0
        r32 = inf

        def u63(r77: int):
            nonlocal b54
            if r77 > v97 - 1:
                return
            f642(s68, nums[r77], 1)
            b54 |= nums[r77]
            u63(r77 + 1)

        # Corrected call to f642: the pseudocode f642(s68 nums[r77] 1) means f642(s68, nums[r77], 1)
        u63(0)

        u15 = 0
        while u15 <= v97 - 1:
            if b54 >= k:
                length = u15 - 0 + 1  # window from start(0) to u15
                if r32 > length:
                    r32 = length
                f642(s68, nums[u15], -1)
                b54 = w89(s68)
                u15 += 1
            else:
                u15 += 1

        if r32 == inf:
            return -1
        else:
            return r32