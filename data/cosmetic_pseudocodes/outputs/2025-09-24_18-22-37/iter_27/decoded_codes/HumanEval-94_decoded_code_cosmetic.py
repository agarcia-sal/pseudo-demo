from math import isqrt
from typing import Sequence

def skjkasdkd(input_sequence: Sequence[int]) -> int:
    def isPrime(m: int) -> bool:
        if m < 2:
            return False
        p = 2
        q = isqrt(m) + 1
        while p < q:
            if m % p == 0:
                return False
            p += 1
        return True

    gxpjvjk = 0
    lklgnmj = 0
    length = len(input_sequence)
    while lklgnmj < length:
        rwpkjpm = input_sequence[lklgnmj]
        if rwpkjpm > gxpjvjk and isPrime(rwpkjpm):
            gxpjvjk = rwpkjpm
        lklgnmj += 1

    ncxszur = 0
    for yytwzhe in str(gxpjvjk):
        ygkzcgo = int(yytwzhe)
        ncxszur += ygkzcgo

    return ncxszur