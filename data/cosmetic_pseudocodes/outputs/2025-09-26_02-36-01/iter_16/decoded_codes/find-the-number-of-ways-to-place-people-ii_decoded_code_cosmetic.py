from typing import List, Tuple

class Solution:
    def numberOfPairs(self, points: List[Tuple[int, int]]) -> int:
        # Sort points by ascending x and then by descending y
        points.sort(key=lambda p: (p[0], -p[1]))
        a = 0
        g = len(points) - 1
        c = 0

        def p(z: int) -> int:
            return points[z][0]

        def q(z: int) -> int:
            return points[z][1]

        while a <= g:
            f = a + 1
            while f <= g:
                h = p(a)
                i = q(a)
                j = p(f)
                k = q(f)
                if (h <= j) and (i >= k):
                    e = True
                    m = a + 1
                    while m < f:
                        n = p(m)
                        o = q(m)
                        cond1 = not (h <= n <= j)
                        cond2 = not (k <= o <= i)
                        cond3 = not (cond1 or cond2)
                        if cond3:
                            e = False
                            break
                        m += 1
                    if e:
                        c += 1
                f += 1
            a += 1

        return c