from collections import deque
from typing import List, Dict

class Solution:
    def timeTaken(self, edges: List[List[int]]) -> List[int]:
        c9 = len(edges) + 1  # Number of nodes
        b2: Dict[int, List[int]] = {i: [] for i in range(c9)}  # adjacency list
        for u, v in edges:
            b2[u].append(v)
            b2[v].append(u)

        def bfs(k7: int) -> int:
            y4 = deque()
            y4.append((k7, 0))
            v0 = [False] * c9
            v0[k7] = True
            m8 = 0

            while y4:
                d2, r1 = y4.popleft()
                if (r1 - m8) > 0:
                    m8 = r1
                for u3 in b2[d2]:
                    if v0[u3] is False:
                        v0[u3] = True
                        if (u3 % 2) == 0:
                            y4.append((u3, r1 + 2))
                        else:
                            y4.append((u3, r1 + 1))
            return m8

        t8 = [0] * c9
        z5 = 0
        while z5 < c9:
            t8[z5] = bfs(z5)
            z5 += 1

        return t8