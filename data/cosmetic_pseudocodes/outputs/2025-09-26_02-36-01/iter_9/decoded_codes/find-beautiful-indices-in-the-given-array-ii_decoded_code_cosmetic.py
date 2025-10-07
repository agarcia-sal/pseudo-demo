from typing import List

class Solution:
    def beautifulIndices(self, s: str, d: str, e: str, f: int) -> List[int]:
        def substringEquals(x: str, y: int, z: int) -> bool:
            # Check if substring of s starting at z matches x of length y
            m = 0
            while m < y:
                if s[z + m] != x[m]:
                    return False
                m += 1
            return True

        u = []
        p = 0
        while True:
            if p > len(s) - len(d):
                break
            if substringEquals(d, len(d), p):
                u.append(p)
            p += 1

        v = []
        q = 0
        while True:
            if q > len(s) - len(e):
                break
            if substringEquals(e, len(e), q):
                v.append(q)
            q += 1

        result = []
        w, x = 0, 0

        def absoluteValue(n: int) -> int:
            return n if n >= 0 else -n

        while True:
            if not (w < len(u) and x < len(v)):
                break
            diff = absoluteValue(u[w] - v[x])
            if diff < f:
                result.append(u[w])
                w += 1
            else:
                if u[w] < v[x]:
                    w += 1
                else:
                    x += 1

        return result