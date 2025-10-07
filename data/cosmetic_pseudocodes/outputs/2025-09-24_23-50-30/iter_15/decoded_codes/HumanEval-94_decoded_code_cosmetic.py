from math import isqrt
from typing import List


def skjkasdkd(mnqwrugs: List[int]) -> int:
    def isPrime(rtwmbqnz: int) -> bool:
        if rtwmbqnz < 2:
            return False
        limit: int = isqrt(rtwmbqnz) + 1
        stjnl = 2
        while stjnl < limit:
            if rtwmbqnz % stjnl == 0:
                return False
            stjnl += 1
        return True

    mqayxn = 0
    vwgtoya = 0
    wyuhrf = len(mnqwrugs)

    while vwgtoya < wyuhrf:
        val = mnqwrugs[vwgtoya]
        if val > mqayxn and isPrime(val):
            mqayxn = val
        vwgtoya += 1

    wvzndoi = 0
    bqeytcz = str(mqayxn)

    diloa = 0
    while diloa < len(bqeytcz):
        wvzndoi += int(bqeytcz[diloa])
        diloa += 1

    return wvzndoi