from typing import List

class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        def orderData(arr: List[List[int]]) -> None:
            # Bubble sort based on the first element of each point
            m = len(arr)
            n = 0
            while (n + 1) < m:
                if arr[n][0] > arr[n + 1][0]:
                    arr[n], arr[n + 1] = arr[n + 1], arr[n]
                    n = -1
                n += 1

        def incrementValue(val: int) -> int:
            return val + 1

        totalRects = 0
        boundary = -2  # 0 - 2 as per pseudocode

        orderData(points)

        index = 0
        while index < len(points):
            px, py = points[index]
            if px > boundary:
                boundary = px + w
                totalRects = incrementValue(totalRects - 1)
            index += 1

        return totalRects