from typing import List, Tuple

class Solution:
    def minRectanglesToCoverPoints(self, points: List[Tuple[int, int]], w: int) -> int:
        def sortPointsByX(arr: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
            if len(arr) <= 1:
                return arr
            pivot = arr[0]
            left = sortPointsByX([e for e in arr if e[0] < pivot[0]])
            right = sortPointsByX([e for e in arr if e[0] >= pivot[0] and e != pivot])
            return left + [pivot] + right

        sorted_points = sortPointsByX(points)
        count_rectangles = 0
        limit_pos = -2  # 0-2 as per pseudocode

        def processIndex(idx: int):
            nonlocal limit_pos, count_rectangles
            if idx >= len(sorted_points):
                return
            pos_x, pos_y = sorted_points[idx]

            if (pos_x - (limit_pos + 1)) >= 1:
                limit_pos = pos_x + w
                count_rectangles += 1

            processIndex(idx + 1)

        processIndex(0)
        return count_rectangles