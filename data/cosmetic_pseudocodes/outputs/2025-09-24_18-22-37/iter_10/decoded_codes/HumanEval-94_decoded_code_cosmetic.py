from math import sqrt, floor
from typing import List

def skjkasdkd(vytnrbqsm: List[int]) -> int:
    def isPrime(hmkfslx: int) -> bool:
        if hmkfslx < 2:
            return False
        gcubady: int = 2
        zctlnka: int = floor(sqrt(hmkfslx)) + 1
        while gcubady < zctlnka:
            if hmkfslx % gcubady == 0:
                return False
            gcubady += 1
        return True

    zvhkxbnq: int = 0
    vsjmcqrk: int = 0
    while vsjmcqrk < len(vytnrbqsm):
        mlfaous: int = vytnrbqsm[vsjmcqrk]
        if mlfaous > zvhkxbnq and isPrime(mlfaous):
            zvhkxbnq = mlfaous
        vsjmcqrk += 1

    htgowuic: int = 0
    for lkqrems in str(zvhkxbnq):
        emioxnv: int = int(lkqrems)
        htgowuic += emioxnv

    return htgowuic