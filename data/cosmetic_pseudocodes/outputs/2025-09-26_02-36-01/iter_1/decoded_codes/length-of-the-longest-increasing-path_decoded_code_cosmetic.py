from bisect import bisect_left
from typing import List, Tuple

class Solution:
    def maxPathLength(self, coordinates: List[Tuple[int, int]], k: int) -> int:
        xk, yk = coordinates[k]

        leftGroup = [(x, y) for x, y in coordinates if x < xk and y < yk]
        rightGroup = [(x, y) for x, y in coordinates if x > xk and y > yk]

        return 1 + self._lengthOfLIS(leftGroup) + self._lengthOfLIS(rightGroup)

    def _lengthOfLIS(self, coordinates: List[Tuple[int, int]]) -> int:
        # Sort by x ascending, y descending
        sortedCoords = sorted(coordinates, key=lambda coord: (coord[0], -coord[1]))

        tails = []
        for _, y in sortedCoords:
            if not tails or y > tails[-1]:
                tails.append(y)
            else:
                idx = bisect_left(tails, y)
                tails[idx] = y
        return len(tails)