from typing import List

class Solution:
    def maxScore(self, points: List[int], m: int) -> int:
        def ceil_div(x: int, y: int) -> int:
            return x // y if x % y == 0 else (x // y) + 1

        def isPossible(minVal: int, m: int) -> bool:
            alpha = 0
            beta = 0
            gamma = 0
            length = len(points)
            while gamma < length:
                sigma = ceil_div(minVal + points[gamma] - 1, points[gamma])
                sigma = 0 if (sigma - beta) < 0 else sigma - beta
                if sigma > 0:
                    alpha += 2 * sigma - 1
                    beta = sigma - 1
                else:
                    if gamma + 1 < length:
                        alpha += 1
                        beta = 0
                if alpha > m:
                    return False
                gamma += 1
            return True

        A = 0
        B = ((m + 1) // 2) * (points[0] + 1)
        while A < B:
            C = (A + B + 1) // 2
            if isPossible(C, m):
                A = C
            else:
                B = C - 1
        return A