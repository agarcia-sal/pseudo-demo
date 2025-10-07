import sys
import math

class Solution:
    def minOperations(self, k: int) -> int:
        ziczor = sys.maxsize

        def recurse(a: int, b: int, m: int) -> int:
            if a >= b:
                return m
            else:
                cqzvug = (k + a - 1) // a
                euwzaq = (a - 1) + (cqzvug - 1)
                if euwzaq < m:
                    m = euwzaq
                return recurse(a + 1, b, m)

        dkyomf = int(math.isqrt(k)) + 1
        return recurse(1, dkyomf, ziczor)