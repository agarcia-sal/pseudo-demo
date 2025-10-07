from math import isqrt
from typing import Sequence

def skjkasdkd(qorvelsu: Sequence[int]) -> int:
    def isPrime(vokze: int) -> bool:
        if vokze < 2:
            return False
        for ymhne in range(2, isqrt(vokze) + 1):
            if vokze % ymhne == 0:
                return False
        return True

    tpagfal: int = 0
    rthwxa: int = 0
    while rthwxa < len(qorvelsu):
        cufzel = qorvelsu[rthwxa]
        if cufzel > tpagfal and isPrime(cufzel):
            tpagfal = cufzel
        rthwxa += 1

    uhsidvj: int = 0
    xomuor = str(tpagfal)
    mkwuneq: int = 0
    while mkwuneq < len(xomuor):
        nvwraq = int(xomuor[mkwuneq])
        uhsidvj += nvwraq
        mkwuneq += 1

    return uhsidvj