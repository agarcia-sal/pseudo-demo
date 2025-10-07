from typing import List

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Solution:
    def numberOfPairs(self, points: List[Point]) -> int:
        m = 0
        totalPoints = len(points)
        u = 0
        while u < totalPoints - 1:
            v = u + 1
            while v < totalPoints:
                ax, ay = points[u].x, points[u].y
                bx, by = points[v].x, points[v].y
                if (not (ax > bx)) and (ay >= by):
                    flag = 1
                    w = u + 1
                    while w <= v - 1:
                        cx, cy = points[w].x, points[w].y
                        if (not (ax > cx)) and (not (cx > bx)) and (by <= cy) and (not (cy > ay)):
                            flag = 0
                            break
                        w += 1
                    if flag == 1:
                        m += 1
                v += 1
            u += 1

        # Bubble sort with specified condition
        while True:
            i = 0
            swapped = False
            while i < totalPoints - 1:
                p_i = points[i]
                p_i1 = points[i+1]
                if (p_i.x > p_i1.x) or (p_i.x == p_i1.x and p_i.y < p_i1.y):
                    points[i], points[i+1] = p_i1, p_i
                    swapped = True
                i += 1
            if not swapped:
                break

        return m