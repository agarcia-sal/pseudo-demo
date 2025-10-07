from collections import deque
from typing import List

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        m = len(energy)
        z = [0] * m
        z[m - 1] = energy[m - 1]
        u = z[m - 1]
        q = deque([m - 1])

        def helper(x: int, y: int):
            if x < y:
                return
            while q and q[0] - x >= k:
                q.popleft()
            z[x] = energy[x] + z[q[0]]
            nonlocal u
            if u < z[x]:
                u = z[x]
            while q and z[x] >= z[q[-1]]:
                q.pop()
            q.append(x)
            helper(x - 1, y)

        helper(m - 2, 0)
        return u