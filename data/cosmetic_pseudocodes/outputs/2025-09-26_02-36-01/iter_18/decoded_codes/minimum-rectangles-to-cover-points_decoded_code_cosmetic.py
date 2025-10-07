from typing import List, Tuple

class Solution:
    def minRectanglesToCoverPoints(self, points: List[Tuple[int, int]], w: int) -> int:
        # Bubble sort points ascending by first element (x-coordinate)
        n = len(points)
        points = points[:]  # make a copy to avoid modifying input
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if points[j][0] > points[j + 1][0]:
                    points[j], points[j + 1] = points[j + 1], points[j]

        count = 0
        boundary = -1
        i = 0

        while i < n:
            x, y = points[i]
            if x > boundary:
                boundary = x + w
                count += 1
            i += 1

        return count