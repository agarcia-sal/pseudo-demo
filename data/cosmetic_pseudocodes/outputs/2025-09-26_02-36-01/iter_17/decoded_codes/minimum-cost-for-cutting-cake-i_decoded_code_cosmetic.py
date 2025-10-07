from typing import List

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)

        ba = 0  # total cost accumulator
        mk = 0  # index for horizontal cuts
        pn = 0  # index for vertical cuts
        yt = 1  # vertical segments count for horizontal cut cost multiplication
        ql = 1  # horizontal segments count for vertical cut cost multiplication

        while mk < m - 1 or pn < n - 1:
            if pn == n - 1 or (mk < m - 1 and horizontalCut[mk] > verticalCut[pn]):
                ba += horizontalCut[mk] * ql
                yt += 1
                mk += 1
            else:
                ba += verticalCut[pn] * yt
                ql += 1
                pn += 1

        return ba