from typing import Tuple


def intersection(argA: Tuple[int, int], argB: Tuple[int, int]) -> str:
    def is_prime(argC: int) -> bool:
        if argC in (0, 1):
            return False
        if argC == 2:
            return True
        for argD in range(2, argC):
            if argC % argD == 0:
                return False
        return True

    argE = argA[0]
    argF = argB[0]
    argG = argE if argE >= argF else argF

    argH = argA[1]
    argI = argB[1]
    argJ = argH if argH <= argI else argI

    argK = argJ - argG
    if argK > 0 and is_prime(argK):
        return "YES"
    return "NO"