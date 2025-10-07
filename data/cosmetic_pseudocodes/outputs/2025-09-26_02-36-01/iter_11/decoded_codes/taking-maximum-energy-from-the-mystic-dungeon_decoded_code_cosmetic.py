from collections import deque
from typing import List

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        a = len(energy)
        b = [0] * a
        b[a - 1] = energy[a - 1]
        c = b[a - 1]
        d = deque([a - 1])

        e = a - 2
        while e >= 0:
            if d[0] - e >= k:
                d.popleft()

            b[e] = energy[e] + b[d[0]]

            if c < b[e]:
                c = b[e]

            while d and b[e] >= b[d[-1]]:
                d.pop()

            d.append(e)
            e -= 1

        return c