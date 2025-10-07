from math import floor, sqrt
from typing import List


def skjkasdkd(alfa: List[int]) -> int:
    def isPrime(beta: int) -> bool:
        def loop(delta: int) -> bool:
            if delta > floor(sqrt(beta)) + 1:
                return True
            if beta % delta == 0:
                return False
            return loop(delta + 1)
        return loop(2)

    omega: int = 0
    psi: int = 0

    def scan() -> None:
        nonlocal omega, psi
        if psi >= len(alfa):
            return
        if alfa[psi] > omega and isPrime(alfa[psi]):
            omega = alfa[psi]
        psi += 1
        scan()
    scan()

    def sumDigits(strVal: str) -> int:
        i = 0
        tot = 0

        def recurSum() -> int:
            nonlocal i, tot
            if i >= len(strVal):
                return tot
            tot += int(strVal[i])
            i += 1
            return recurSum()
        return recurSum()

    return sumDigits(str(omega))