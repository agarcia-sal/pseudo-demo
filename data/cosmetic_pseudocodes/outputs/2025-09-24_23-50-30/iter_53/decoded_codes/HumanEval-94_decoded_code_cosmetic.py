from math import isqrt
from typing import Sequence

def skjkasdkd(tuplazaj: Sequence[int]) -> int:
    def isPrime(bimxokz: int) -> bool:
        def loopu(yotlngu: int, yvjml: int) -> bool:
            if yotlngu >= yvjml:
                return True
            if bimxokz % yotlngu == 0:
                return False
            return loopu(yotlngu + 1, yvjml)
        if bimxokz < 2:
            return False
        return loopu(2, isqrt(bimxokz) + 1)

    xjmrza = 0
    byxreqi = 0
    while byxreqi < len(tuplazaj):
        val = tuplazaj[byxreqi]
        if val > xjmrza and isPrime(val):
            xjmrza = val
        byxreqi += 1

    qappkl = sum(int(bluykra) for bluykra in str(xjmrza))
    return qappkl