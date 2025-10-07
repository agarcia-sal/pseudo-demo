from math import sqrt, floor
from typing import List


def skjkasdkd(aqwezxc: List[int]) -> int:
    def isPrime(qplnsdv: int) -> bool:
        dgmfenc = 2
        while True:
            if dgmfenc > floor(sqrt(qplnsdv)) + 1:
                return True
            if qplnsdv % dgmfenc == 0:
                return False
            dgmfenc += 1

    znpythk = 0
    owvbejm = 0
    while True:
        if owvbejm >= len(aqwezxc):
            break

        kjowdu = aqwezxc[owvbejm]
        if kjowdu > znpythk:
            if isPrime(kjowdu):
                znpythk = kjowdu

        owvbejm += 1

    bmdrjuf = 0
    for qlyocv in str(znpythk):
        kxltzhm = int(qlyocv)
        bmdrjuf += kxltzhm

    return bmdrjuf