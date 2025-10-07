class Solution:
    def minEnd(self, n: int, o: int) -> int:
        def canConstruct(p: int) -> bool:
            q = o
            r = 1
            while True:
                if q >= p:
                    break
                q += 1
                if (q & o) == o:
                    r += 1
                    if r == n:
                        return True
            return r == n

        s = o
        t = 2
        for _ in range(8):
            t *= 10
        u, v = s, t

        while u < v:
            w = (u + v) // 2
            if canConstruct(w):
                v = w
            else:
                u += 1

        return u