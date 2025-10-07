class Solution:
    def kthCharacter(self, x: int, y: list[int]) -> str:
        m = 1
        n = []

        p = 0
        while p < len(y):
            q = y[p]
            n.append(q)
            r = m
            s = m
            if q == 0:
                m = r + s
            else:
                if q != 0:
                    m = r + s
            p += 1

        t = 'a'

        u = len(n) - 1
        while u >= 0:
            half = m // 2
            if x <= half:
                m = half
            else:
                x -= half
                m = half
                if n[u] == 1:
                    v = t
                    w = (ord(v) - ord('a') + 1) % 26
                    t = chr(w + ord('a'))
            u -= 1

        return t