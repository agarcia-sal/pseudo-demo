class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        def cyclic_distance(c1: str, c2: str) -> int:
            x = abs(ord(c1) - ord(c2))
            y = 26 - x
            return y if y < x else x

        p = list(s)
        m = len(s)
        q = 0

        while k > 0 and q < m:
            if p[q] == 'a':
                q += 1
                continue
            r = cyclic_distance(p[q], 'a')
            if r <= k:
                p[q] = 'a'
                k -= r
            else:
                p[q] = chr(ord(p[q]) - k)
                k = 0
            q += 1

        return ''.join(p)