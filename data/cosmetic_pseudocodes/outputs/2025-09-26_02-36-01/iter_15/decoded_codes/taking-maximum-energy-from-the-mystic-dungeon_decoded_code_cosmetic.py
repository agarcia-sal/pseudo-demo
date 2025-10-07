from collections import deque
from typing import List

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        q = deque()
        m = len(energy)
        f = [0] * m
        res = energy[m - 1]
        f[m - 1] = energy[m - 1]
        q.append(m - 1)

        idx = m - 2
        while idx >= 0:
            while q and (q[0] - idx) >= k:
                q.popleft()

            val1 = energy[idx]
            val2 = f[q[0]]
            total = val1 + val2
            f[idx] = total

            if res < total:
                res = total

            while q and f[q[-1]] <= f[idx]:
                q.pop()

            q.append(idx)
            idx -= 1

        return res