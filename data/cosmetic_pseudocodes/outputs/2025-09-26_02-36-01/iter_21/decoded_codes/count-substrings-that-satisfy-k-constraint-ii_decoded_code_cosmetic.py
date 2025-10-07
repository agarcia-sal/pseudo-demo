from typing import List

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:
        a = len(s)
        b = a + 1
        c = [0] * b  # prefix sums of '0's
        d = [0] * b  # prefix sums of '1's

        def e(f: int, g: int) -> int:
            h = 0
            i = f
            while i <= g:
                j = i
                m = g + 1
                n = j
                while n < m:
                    o = (n + m) // 2
                    p = c[o + 1] - c[j]
                    q = d[o + 1] - d[j]
                    if p <= k or q <= k:
                        n = o + 1
                    else:
                        m = o
                r = n - 1
                if r >= j:
                    h += (r - j + 1)
                i += 1
            return h

        s1 = 0
        while s1 < a:
            c[s1 + 1] = c[s1] + (1 if s[s1] == '0' else 0)
            d[s1 + 1] = d[s1] + (1 if s[s1] == '1' else 0)
            s1 += 1

        t = []
        u = 0
        while u < len(queries):
            v = queries[u][0]
            w = queries[u][1]
            x = e(v, w)
            t.append(x)
            u += 1

        return t