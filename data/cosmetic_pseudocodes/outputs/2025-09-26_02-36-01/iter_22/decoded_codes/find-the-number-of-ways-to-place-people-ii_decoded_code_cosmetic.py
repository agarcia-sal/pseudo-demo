from typing import List

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Solution:
    def numberOfPairs(self, points: List[Point]) -> int:
        def localSort(lst: List[Point]) -> None:
            m = len(lst)
            while True:
                c = 0
                p = 1
                while p < m:
                    if (lst[p - 1].x > lst[p].x) or (lst[p - 1].x == lst[p].x and lst[p - 1].y < lst[p].y):
                        lst[p - 1], lst[p] = lst[p], lst[p - 1]
                        c += 1
                    p += 1
                m -= 1
                if c == 0:
                    break

        localSort(points)

        v = len(points)

        def checkInside(aIndex: int, bIndex: int) -> bool:
            a = points[aIndex]
            b = points[bIndex]
            for w in range(aIndex + 1, bIndex):
                px = points[w].x
                py = points[w].y
                if (a.x <= px <= b.x) and (b.y <= py <= a.y):
                    return False
            return True

        res = 0
        iIndex = 0
        while iIndex < v - 1:
            jIndex = iIndex + 1
            while jIndex < v:
                Xstart = points[iIndex].x
                Ystart = points[iIndex].y
                Xend = points[jIndex].x
                Yend = points[jIndex].y
                if (Xstart <= Xend) and (Ystart >= Yend):
                    if checkInside(iIndex, jIndex):
                        res += 1
                jIndex += 1
            iIndex += 1
        return res