from typing import List

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        q = len(nums)
        r = [[1] * (k + 1) for _ in range(q)]
        s = 0
        for p, w in enumerate(nums):
            for t in range(k + 1):
                u = 0
                while u < p:
                    v = nums[u]
                    if w == v:
                        tmp1 = r[p][t]
                        tmp2 = r[u][t + 1] if t + 1 <= k else 1
                        if tmp1 < tmp2:
                            r[p][t] = tmp2
                    elif t > 0:
                        a1 = r[p][t]
                        a2 = r[u][t - 1] + 1
                        if a1 < a2:
                            r[p][t] = a2
                    u += 1
            if r[p][k] > s:
                s += r[p][k] - s
        return s