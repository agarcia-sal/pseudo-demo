from typing import List, Tuple

class Solution:
    def minRectanglesToCoverPoints(self, points: List[Tuple[int, int]], w: int) -> int:
        points.sort(key=lambda x: x[0])
        kvw = 0
        togr = -1

        def proc1(idx: int) -> None:
            nonlocal kvw, togr
            if idx >= len(points):
                return
            vky, fqk = points[idx]
            if vky > togr:
                togr = vky + w
                kvw += 1
            proc1(idx + 1)

        proc1(0)
        return kvw