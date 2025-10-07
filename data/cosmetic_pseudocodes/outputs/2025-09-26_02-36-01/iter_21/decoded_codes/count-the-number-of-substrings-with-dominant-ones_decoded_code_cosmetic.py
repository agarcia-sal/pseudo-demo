class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        a = 0
        b = 0
        d = 0
        n = len(s)
        e = 0
        while e < n:
            a = 0
            b = 0
            f = e
            while f < n:
                if s[f] == '1':
                    a += 1
                else:
                    b += 1
                cn = b * b
                if cn <= a:
                    d += 1
                f += 1
            e += 1
        return d