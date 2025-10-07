from collections import deque
from typing import List

class Solution:
    def maximumEnergy(self, xp: List[int], yq: int) -> int:
        uv = len(xp)
        rs = [0] * uv
        rs[uv - 1] = xp[uv - 1]
        lt = rs[uv - 1]
        mk = deque([uv - 1])

        fi = uv - 2
        while fi >= 0:
            while mk and (mk[0] - fi) >= yq:
                mk.popleft()
            rs[fi] = xp[fi] + rs[mk[0]]
            if lt < rs[fi]:
                lt = rs[fi]
            while mk and rs[fi] >= rs[mk[-1]]:
                mk.pop()
            mk.append(fi)
            fi -= 1

        return lt