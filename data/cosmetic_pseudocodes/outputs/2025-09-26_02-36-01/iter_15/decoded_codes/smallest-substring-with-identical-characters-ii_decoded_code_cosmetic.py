class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        def check(m: int) -> bool:
            a = 0
            b = 0
            j = 0
            n = len(s)
            while j < n:
                b += 1
                if j == n - 1 or s[j] != s[j + 1]:
                    a += ((b - 1) // m) + 1
                    if a > numOps:
                        return False
                    b = 0
                j += 1
            return a <= numOps

        p = len(s)
        q = 1
        r = p
        while q < r:
            o = (q + r) // 2
            if check(o):
                r = o
            else:
                q = o + 1
        return q