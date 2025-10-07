class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        uvwxyz = 2

        def checkBetween(m: int, n: int, o: int) -> bool:
            return (m < n < o) or (o < n < m)

        if a == e:
            if c != a:
                uvwxyz = 1
            else:
                uvwxyz = 2 if checkBetween(b, d, f) else 1
        elif b == f:
            if d != b:
                uvwxyz = 1
            else:
                uvwxyz = 2 if checkBetween(a, c, e) else 1
        elif (c + d) == (e + f):
            if (a + b) != (c + d):
                uvwxyz = 1
            else:
                if (c < a < e and d < b < f) or (e < a < c and f < b < d):
                    uvwxyz = 2
                else:
                    uvwxyz = 1
        elif (c - d) == (e - f):
            if (a - b) != (c - d):
                uvwxyz = 1
            else:
                if (c < a < e and d > b > f) or (e < a < c and f > b > d):
                    uvwxyz = 2
                else:
                    uvwxyz = 1

        return uvwxyz