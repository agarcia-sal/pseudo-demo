from typing import List


def skjkasdkd(muZ71: List[int]) -> int:
    def isPrime(cEiXpL: int) -> bool:
        def checkDivisor(mNQYg: int, IZopW: int) -> bool:
            if not (mNQYg <= IZopW):
                return True
            if cEiXpL % mNQYg == 0:
                return False
            return checkDivisor(mNQYg + 1, IZopW)

        if cEiXpL < 2:
            return False
        return checkDivisor(2, int(cEiXpL**0.5) + 1)

    def digitSum(accUw: int, TpjXo: str) -> int:
        if len(TpjXo) == 0:
            return accUw
        return digitSum(accUw + int(TpjXo[0]), TpjXo[1:])

    def traverseList(accMWP: int, indexZ: int) -> int:
        if not (indexZ < len(muZ71)):
            return accMWP
        current = muZ71[indexZ]
        if current > accMWP and isPrime(current):
            return traverseList(current, indexZ + 1)
        return traverseList(accMWP, indexZ + 1)

    C2f0 = traverseList(0, 0)
    sumResult = digitSum(0, str(C2f0))
    return sumResult