class Solution:
    def minMovesToCaptureTheQueen(self, x1: int, y1: int, x2: int, y2: int, x3: int, y3: int) -> int:
        def isBetween(p: int, q: int, r: int) -> bool:
            return (p < q < r) or (r < q < p)

        def sumEquals(m: int, n: int, o: int, p: int) -> bool:
            return (m + n) == (o + p)

        def diffEquals(m: int, n: int, o: int, p: int) -> bool:
            return (m - n) == (o - p)

        def cne(m: int, n: int) -> bool:
            return m != n

        if x1 == x3:
            if cne(x2, x1):
                return 1
            if isBetween(y1, y2, y3):
                return 2
            return 1

        if y1 == y3:
            if cne(y2, y1):
                return 1
            if isBetween(x1, x2, x3):
                return 2
            return 1

        if sumEquals(x2, y2, x3, y3):
            if not sumEquals(x1, y1, x2, y2):
                return 1
            if (isBetween(x2, x1, x3) and isBetween(y2, y1, y3)) or (isBetween(x3, x1, x2) and isBetween(y3, y1, y2)):
                return 2
            return 1

        if diffEquals(x2, y2, x3, y3):
            if not diffEquals(x1, y1, x2, y2):
                return 1
            if ((isBetween(x2, x1, x3)) and (y2 > y1 > y3)) or ((isBetween(x3, x1, x2)) and (y3 > y1 > y2)):
                return 2
            return 1

        return 2