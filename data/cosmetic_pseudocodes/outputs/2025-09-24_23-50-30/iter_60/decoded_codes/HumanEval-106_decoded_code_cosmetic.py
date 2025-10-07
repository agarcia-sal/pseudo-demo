from typing import List


def f(x0: int) -> List[int]:
    def innerSum(y3: int, z8: int) -> int:
        if z8 > y3:
            return 0
        else:
            return z8 + innerSum(y3, z8 + 1)

    def innerProduct(q1: int, r6: int) -> int:
        if r6 > q1:
            return 1
        else:
            return r6 * innerProduct(q1, r6 + 1)

    def loop(u7: int, v5: List[int]) -> List[int]:
        if u7 > x0:
            return v5
        if u7 % 2 == 0:
            w4 = innerProduct(u7, 1)
            return loop(u7 + 1, v5 + [w4])
        else:
            w4 = innerSum(u7, 1)
            return loop(u7 + 1, v5 + [w4])

    return loop(1, [])