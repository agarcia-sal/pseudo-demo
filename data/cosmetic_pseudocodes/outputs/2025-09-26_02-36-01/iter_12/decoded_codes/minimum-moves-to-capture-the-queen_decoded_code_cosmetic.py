class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        # Helper procedure to swap values if x > y
        def swapIfGreater(x: int, y: int):
            if x > y:
                return y, x
            return x, y

        # Helper function to check if val lies strictly between start and end
        def isBetween(val: int, start: int, end: int) -> bool:
            low, high = swapIfGreater(start, end)
            return low < val < high

        if a == e:
            if c != a:
                return 1
            else:
                if isBetween(d, b, f) or isBetween(d, f, b):
                    return 2
                else:
                    return 1

        if b == f:
            if d != b:
                return 1
            else:
                if isBetween(c, a, e) or isBetween(c, e, a):
                    return 2
                else:
                    return 1

        sumCD = c + d
        sumEF = e + f

        if sumCD == sumEF:
            if (a + b) != sumCD:
                return 1
            else:
                if (c < a < e and d < b < f) or (e < a < c and f < b < d):
                    return 2
                else:
                    return 1

        diffCD = c - d
        diffEF = e - f

        if diffCD == diffEF:
            if (a - b) != diffCD:
                return 1
            else:
                if (c < a < e and d > b > f) or (e < a < c and f > b > d):
                    return 2
                else:
                    return 1

        return 2