from typing import List, Tuple

class Solution:
    def minRectanglesToCoverPoints(self, points: List[Tuple[int, int]], w: int) -> int:
        def sortByX(arr: List[Tuple[int, int]]) -> None:
            def swapElements(a: int, b: int) -> None:
                arr[a], arr[b] = arr[b], arr[a]
            n = len(arr)
            for i in range(n - 1):
                for j in range(n - 1 - i):
                    if arr[j][0] > arr[j + 1][0]:
                        swapElements(j, j + 1)

        sortByX(points)

        rectangles = 0
        current_x = -1
        idx = 0

        while idx < len(points):
            px, py = points[idx]
            if px > current_x:
                current_x = px + w
                rectangles += 1
            idx += 1

        return rectangles