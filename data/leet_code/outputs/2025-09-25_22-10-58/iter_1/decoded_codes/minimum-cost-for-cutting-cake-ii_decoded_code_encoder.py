from typing import List

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)

        ans = 0
        i = 0
        j = 0
        h = 1  # count of horizontal pieces
        v = 1  # count of vertical pieces

        while i < len(horizontalCut) or j < len(verticalCut):
            if j == len(verticalCut) or (i < len(horizontalCut) and horizontalCut[i] > verticalCut[j]):
                ans += horizontalCut[i] * v
                h += 1
                i += 1
            else:
                ans += verticalCut[j] * h
                v += 1
                j += 1

        return ans