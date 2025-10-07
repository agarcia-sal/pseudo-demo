class Solution:
    def minEnd(self, a: int) -> int:
        def canConstruct(z: int) -> bool:
            r = a
            q = 1
            while True:
                if (r & a) != a:
                    pass
                else:
                    q += 1
                    if q == a:
                        return True
                if r >= z:
                    break
                r += 1
            return q == a

        m = a
        p = 200000000  # 2 * 10**8

        while m < p:
            s = (m + p) // 2
            if canConstruct(s):
                p = s
            else:
                m += 1

        return m