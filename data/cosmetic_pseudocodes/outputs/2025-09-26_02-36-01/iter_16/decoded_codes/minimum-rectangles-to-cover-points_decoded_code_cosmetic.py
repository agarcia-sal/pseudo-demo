from typing import List, Tuple

class Solution:
    def minRectanglesToCoverPoints(self, points: List[Tuple[int, int]], w: int) -> int:
        res = 0
        curPos = -1
        idx = 0
        while idx < len(points):
            pnt = points[idx]
            if not (pnt[0] <= curPos):
                curPos = pnt[0] + w
                res += 1
            else:
                _ = 1  # dummy operation
            idx += 1
        self.sortPointsByX(points)
        return res

    def sortPointsByX(self, arr: List[Tuple[int, int]]) -> None:
        n = len(arr)
        i = 0
        while i < n - 1:
            j = 0
            while j < n - i - 1:
                if arr[j][0] > arr[j + 1][0]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                j += 1
            i += 1