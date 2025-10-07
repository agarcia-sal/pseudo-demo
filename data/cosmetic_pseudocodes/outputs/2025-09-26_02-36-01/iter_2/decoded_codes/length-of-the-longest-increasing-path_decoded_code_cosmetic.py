from bisect import bisect_left
from typing import List, Tuple, Optional


class Solution:
    def maxPathLength(self, points: List[Tuple[int, int]], index: int) -> int:
        pivotX = points[index][0]
        pivotY = points[index][1]

        lesserSide = []
        i = 0
        while i < len(points):
            currX, currY = points[i]
            if currX < pivotX and currY < pivotY:
                lesserSide.append((currX, currY))
            i += 1

        greaterSide = []
        j = 0
        while j < len(points):
            px, py = points[j]
            if not (px <= pivotX or py <= pivotY):
                greaterSide.append((px, py))
            j += 1

        leftLen = self._lengthOfLIS(lesserSide)
        rightLen = self._lengthOfLIS(greaterSide)

        return 1 + leftLen + rightLen

    def _lengthOfLIS(self, coords: List[Tuple[int, int]]) -> int:
        sortedCoords = sorted(coords, key=lambda a: (a[0], -a[1]))
        subsequence = []
        idx = 0
        while idx < len(sortedCoords):
            currentY = sortedCoords[idx][1]
            if not subsequence or subsequence[-1] < currentY:
                subsequence.append(currentY)
            else:
                replacePos = bisect_left(subsequence, currentY)
                subsequence[replacePos] = currentY
            idx += 1
        return len(subsequence)