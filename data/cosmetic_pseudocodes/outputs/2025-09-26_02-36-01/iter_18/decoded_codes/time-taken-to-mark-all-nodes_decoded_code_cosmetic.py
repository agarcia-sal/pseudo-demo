from collections import deque
from typing import List

class Solution:
    def timeTaken(self, edges: List[int]) -> List[int]:
        p0z = len(edges) + 1
        u2y = [[] for _ in range(p0z)]

        for i, parent in enumerate(edges, start=1):
            u2y[parent].append(i)

        def bfs(vxq: int) -> int:
            ylh = deque()
            ylh.append((vxq, 0))
            mwr = [False] * p0z
            mwr[vxq] = True
            bsf = 0

            while ylh:
                r1k, g8j = ylh.popleft()
                if bsf < g8j:
                    bsf = g8j

                for t93 in u2y[r1k]:
                    if not mwr[t93]:
                        mwr[t93] = True
                        if t93 % 2 == 0:
                            ylh.append((t93, g8j + 2))
                        else:
                            ylh.append((t93, g8j + 1))
            return bsf

        oe5 = [0] * p0z
        for a9k in range(p0z):
            oe5[a9k] = bfs(a9k)

        return oe5