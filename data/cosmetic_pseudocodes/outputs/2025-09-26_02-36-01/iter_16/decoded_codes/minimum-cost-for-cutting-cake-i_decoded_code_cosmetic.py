from typing import List

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        horizontalCut.sort(reverse=True)  # Sort descending
        verticalCut.sort(reverse=True)    # Sort descending

        i = 0  # pointer for horizontal cuts
        j = 0  # pointer for vertical cuts
        horizontal_segments = 1
        vertical_segments = 1
        ans = 0

        while i < m - 1 or j < n - 1:
            if j < n - 1 and (i >= m - 1 or verticalCut[j] >= horizontalCut[i]):
                ans += verticalCut[j] * horizontal_segments
                vertical_segments += 1
                j += 1
            else:
                ans += horizontalCut[i] * vertical_segments
                horizontal_segments += 1
                i += 1

        return ans