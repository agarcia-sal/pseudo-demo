from typing import List

def f(x: int) -> List[int]:
    def func(accum: List[int], y: int) -> List[int]:
        z = 1
        w = 0
        if y % 2 == 0:
            k = 1
            while k <= y:
                z *= k
                k += 1
            return accum + [z]
        else:
            m = 1
            while m <= y:
                w += m
                m += 1
            return accum + [w]

    accum: List[int] = []
    for y in range(1, x + 1):
        accum = func(accum, y)
    return accum