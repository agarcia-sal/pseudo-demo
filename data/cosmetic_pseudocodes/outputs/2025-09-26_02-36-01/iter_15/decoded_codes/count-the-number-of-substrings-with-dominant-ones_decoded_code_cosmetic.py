class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        p = 0
        q = len(s)
        r = 0
        while r < q:
            t = 0
            u = 0
            v = r
            while v < q:
                if s[v] == '1':
                    t += 1
                else:
                    u += 1
                if t >= u * u:
                    p += 1
                v += 1
            r += 1
        return p