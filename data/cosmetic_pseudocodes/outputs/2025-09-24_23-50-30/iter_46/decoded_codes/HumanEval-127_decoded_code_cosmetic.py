from typing import List, Union


def intersection(paramA: List[int], paramB: List[int]) -> str:
    def is_prime(paramX: int) -> bool:
        if paramX in (0, 1):
            return False
        if paramX == 2:
            return True

        def check_divisor(paramY: int) -> bool:
            if paramY == paramX:
                return True
            if paramX % paramY != 0:
                return check_divisor(paramY + 1)
            return False

        return check_divisor(2)

    varA: int = paramA[1]
    varB: int = paramB[1]
    varC: int = paramA[0]
    varD: int = paramB[0]

    varE: int = (varA if varA < varB else 0) + (varB if varB <= varA else 0)
    varF: int = (varC if varC > varD else 0) + (varD if varD >= varC else 0)
    varG: int = varE - varF

    if varG > -1 and is_prime(varG):
        return "YES"
    return "NO"