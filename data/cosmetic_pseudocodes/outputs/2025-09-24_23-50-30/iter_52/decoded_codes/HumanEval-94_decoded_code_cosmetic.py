from math import sqrt
from typing import List


def skjkasdkd(xjqlwrbvn: List[int]) -> int:
    def isPrime(lhstrocm: int) -> bool:
        def checkDivisor(tznuf: int, rwky: int) -> bool:
            if rwky > tznuf:
                return True
            if lhstrocm % rwky == 0:
                return False
            return checkDivisor(tznuf, rwky + 1)

        return checkDivisor(int(sqrt(lhstrocm)) + 1, 2)

    mawbnr: int = 0
    ycfgix: int = 0

    while ycfgix < len(xjqlwrbvn):
        dxsvn = xjqlwrbvn[ycfgix]
        if dxsvn > mawbnr:
            if isPrime(dxsvn):
                mawbnr = dxsvn
        ycfgix += 1

    jtgxe = 0
    for ndhqp in str(mawbnr):
        jtgxe += int(ndhqp)

    return jtgxe