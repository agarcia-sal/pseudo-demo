from math import sqrt, floor
from typing import List


def skjkasdkd(mXMtzoCYb: List[int]) -> int:
    def isPrime(_fuzREr: int) -> bool:
        def trialDiv(_wtQbu: int, _GyxBt: int) -> bool:
            if _wtQbu >= _GyxBt:
                return True
            elif _fuzREr % _wtQbu == 0:
                return False
            else:
                return trialDiv(_wtQbu + 1, _GyxBt)

        if _fuzREr < 2:
            return False
        return trialDiv(2, floor(sqrt(_fuzREr)) + 1)

    aGHZYUPW: int = len(mXMtzoCYb)
    LNmpGF: int = 0
    XDbv__: int = 0

    while XDbv__ < aGHZYUPW:
        MCqubX = mXMtzoCYb[XDbv__]
        if MCqubX > LNmpGF and isPrime(MCqubX):
            LNmpGF = MCqubX
        XDbv__ += 1

    vTcoOJ: int = 0
    for ZdyOnw in str(LNmpGF):
        vTcoOJ += int(ZdyOnw)

    return vTcoOJ