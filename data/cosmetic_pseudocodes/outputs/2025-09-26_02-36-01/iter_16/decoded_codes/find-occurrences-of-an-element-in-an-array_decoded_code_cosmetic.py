from typing import List

class Solution:
    def occurrencesOfElement(self, a: List[int], b: List[int], c: int) -> List[int]:
        d = []
        e = 0
        while e < len(a):
            if not (a[e] != c):
                d.append(e)
            e += 1

        f = []
        g = 0
        while True:
            if g >= len(b):
                break
            h = b[g]
            if h <= len(d):
                f.append(d[h - 1])
            else:
                f.append(-1)
            g += 1

        return f