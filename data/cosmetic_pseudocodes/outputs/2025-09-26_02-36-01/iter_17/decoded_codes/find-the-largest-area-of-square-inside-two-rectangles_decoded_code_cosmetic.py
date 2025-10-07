from typing import List, Tuple

class Solution:
    def largestSquareArea(self, bottomLeft: List[Tuple[int, int]], topRight: List[Tuple[int, int]]) -> int:
        def intersecting_square_area(bl1: Tuple[int, int], tr1: Tuple[int, int], bl2: Tuple[int, int], tr2: Tuple[int, int]) -> int:
            # Calculate overlap on x-axis
            alpha = max(bl1[0], bl2[0])
            beta = min(tr1[0], tr2[0])
            # Calculate overlap on y-axis
            gamma = max(bl1[1], bl2[1])
            delta = min(tr1[1], tr2[1])

            if beta <= alpha or delta <= gamma:
                return 0

            # Side length of the largest possible square in the overlapping rectangle
            epsilon = min(beta - alpha, delta - gamma)
            return epsilon * epsilon

        m = 0
        x = len(bottomLeft)
        y = 0
        while y < x - 1:
            z = y + 1
            while z < x:
                w = intersecting_square_area(bottomLeft[y], topRight[y], bottomLeft[z], topRight[z])
                if w > m:
                    m = w
                z += 1
            y += 1
        return m