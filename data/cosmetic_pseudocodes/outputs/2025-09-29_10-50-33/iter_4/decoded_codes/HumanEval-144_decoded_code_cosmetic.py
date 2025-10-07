from typing import Tuple


def simplify(fraction_A: str, fraction_B: str) -> bool:
    numeratorPart1: str = ""
    denominatorPart1: str = ""
    numeratorPart2: str = ""
    denominatorPart2: str = ""

    for idx in range(len(fraction_A)):
        if fraction_A[idx] == "/":
            numeratorPart1 = fraction_A[:idx]
            denominatorPart1 = fraction_A[idx + 1 :]
            break

    for pos in range(len(fraction_B)):
        if fraction_B[pos] == "/":
            numeratorPart2 = fraction_B[:pos]
            denominatorPart2 = fraction_B[pos + 1 :]
            break

    multipliedNum: int = int(numeratorPart1) * int(numeratorPart2)
    multipliedDen: int = int(denominatorPart1) * int(denominatorPart2)

    division_result: float = multipliedNum / multipliedDen
    if division_result == int(division_result):
        return True
    return False