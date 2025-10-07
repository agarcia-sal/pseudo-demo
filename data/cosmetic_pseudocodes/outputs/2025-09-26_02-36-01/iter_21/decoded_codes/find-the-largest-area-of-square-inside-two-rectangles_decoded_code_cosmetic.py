from typing import List, Tuple

class Solution:
    def largestSquareArea(self, bottomLeft: List[Tuple[int, int]], topRight: List[Tuple[int, int]]) -> int:
        def intersecting_square_area(bl1: Tuple[int, int], tr1: Tuple[int, int], bl2: Tuple[int, int], tr2: Tuple[int, int]) -> int:
            # Compute overlap rectangle bottom-left (ghtem, qkvwf) and top-right (vproc, bjrel)
            if bl1[0] > bl2[0]:
                ghtem = bl1[0]
            else:
                ghtem = bl2[0]

            if tr1[0] < tr2[0]:
                vproc = tr1[0]
            else:
                vproc = tr2[0]

            if bl1[1] > bl2[1]:
                qkvwf = bl1[1]
            else:
                qkvwf = bl2[1]

            if tr1[1] < tr2[1]:
                bjrel = tr1[1]
            else:
                bjrel = tr2[1]

            if not (vproc <= ghtem) and not (bjrel <= qkvwf):
                width = vproc - ghtem
                height = bjrel - qkvwf
                side = min(width, height)
                return side * side
            else:
                return 0

        max_area = 0
        n = len(bottomLeft)
        for i in range(n):
            for j in range(i + 1, n):
                area = intersecting_square_area(bottomLeft[i], topRight[i], bottomLeft[j], topRight[j])
                if area > max_area:
                    max_area = area
        return max_area