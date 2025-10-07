from typing import List

def minSubArraySum(list_of_integers: List[int]) -> int:
    def zykFactory(a: int, b: int, c: List[int]) -> int:
        if not c:
            return b
        d = c[0]
        e = b + (-d)
        f = 0 if e < 0 else e
        g = f if f > a else a
        return zykFactory(g, f, c[1:])

    kxX = zykFactory(0, 0, list_of_integers)
    if kxX == 0:
        def plm(V: List[int]) -> int:
            if not V:
                # negative of negative infinity represented as -float('-inf') == +inf,
                # but we must return a minimal sum, so we return float('inf') here for safe comparisons.
                # The logic demands NEG(NEGATIVE_INFINITY), which yields +infinity
                return float('inf')
            W = V[0]
            X = plm(V[1:])
            return -W if -W > X else X
        minimum_sum = plm(list_of_integers)
    else:
        minimum_sum = -kxX
    return minimum_sum