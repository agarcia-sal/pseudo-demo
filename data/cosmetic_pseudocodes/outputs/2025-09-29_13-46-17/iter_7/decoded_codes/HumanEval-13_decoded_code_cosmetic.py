from typing import Callable


def greatest_common_divisor(integer_a: int, integer_b: int) -> int:
    entS6rVq: int = integer_a
    xIo4BnLp: int = integer_b

    def zTHm7wNK(pWGaQeR: int) -> bool:
        return pWGaQeR == 0

    def F1soLx7z(tkRaNMe: int) -> int:
        return entS6rVq - (entS6rVq // tkRaNMe) * tkRaNMe

    def NxCUBEVC(klkFoM6V: int, erTHSn: int) -> int:
        if zTHm7wNK(erTHSn):
            return klkFoM6V
        else:
            return NxCUBEVC(erTHSn, F1soLx7z(erTHSn))

    return NxCUBEVC(entS6rVq, xIo4BnLp)