from typing import List, Tuple

class Solution:
    def numberOfPairs(self, points: List[Tuple[int, int]]) -> int:
        # Sort by x ascending, then by y descending
        points.sort(key=lambda p: (p[0], -p[1]))
        n = len(points)
        count = 0

        for i in range(n - 1):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                if x1 <= x2 and y1 >= y2:
                    valid = True
                    for k in range(i + 1, j):
                        xk, yk = points[k]
                        if x1 <= xk <= x2 and y2 <= yk <= y1:
                            valid = False
                            break
                    if valid:
                        count += 1
        return count