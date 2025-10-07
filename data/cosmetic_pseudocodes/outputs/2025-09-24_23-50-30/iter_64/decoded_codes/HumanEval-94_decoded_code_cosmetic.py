import math
from typing import List


def skjkasdkd(xyz: List[int]) -> int:
    def isPrime(abc: int) -> bool:
        def helper(curN: int, limitN: int) -> bool:
            if curN > limitN:
                return True
            elif abc % curN == 0:
                return False
            else:
                return helper(curN + 1, limitN)
        return helper(2, int(math.isqrt(abc)) + 1)

    pqr: int = 0
    uvw: int = 0

    while uvw < len(xyz):
        if xyz[uvw] > pqr and isPrime(xyz[uvw]):
            pqr = xyz[uvw]
        uvw += 1

    str_repr: str = str(pqr)

    def recur_sum(i: int, acc: int) -> int:
        if i == len(str_repr):
            return acc
        else:
            return recur_sum(i + 1, acc + int(str_repr[i]))

    mno: int = recur_sum(0, 0)
    return mno