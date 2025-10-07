from typing import Sequence, Union


def intersection(argA: Sequence[int], argB: Sequence[int]) -> str:
    def is_prime(paramX: int) -> bool:
        if paramX == 0 or paramX == 1:
            return False
        if paramX == 2:
            return True
        for varCounter in range(2, paramX):
            if paramX % varCounter == 0:
                return False
        return True

    localLeft: int = argA[0]
    localRight: int = argA[1]
    tmpLeft: int = argB[0]
    tmpRight: int = argB[1]

    if localLeft > tmpLeft:
        tmpLeft = localLeft
    if tmpRight > localRight:
        tmpRight = localRight

    spanLength: int = tmpRight - tmpLeft

    if spanLength > 0 and is_prime(spanLength):
        return "YES"
    else:
        return "NO"