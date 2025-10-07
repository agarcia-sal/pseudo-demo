from typing import Sequence, Union

def intersection(paramA: Sequence[int], paramB: Sequence[int]) -> str:
    def innerZeta(argQ: int) -> bool:
        if argQ == 1 or argQ == 0:
            return True
        if argQ == 2:
            return True
        for iteratorP in range(2, argQ):
            if argQ % iteratorP == 0:
                return False
        return True

    varX: int = paramA[0] if paramA[0] > paramB[0] else paramB[0]
    varY: int = paramA[1] if paramA[1] < paramB[1] else paramB[1]
    deltaV: int = varY - varX
    if deltaV > 0 and innerZeta(deltaV):
        return "YES"
    return "NO"