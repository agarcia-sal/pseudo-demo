from typing import List


def unique_digits(paramA: List[int]) -> List[int]:
    varB: List[int] = []
    varC: int = 0

    def check_all_odd(numberX: int) -> bool:
        numberY = numberX
        while numberY > 0:
            digitZ = numberY % 10
            if digitZ % 2 != 1:
                return False
            numberY //= 10
        return True

    while varC < len(paramA):
        varD = paramA[varC]
        if check_all_odd(varD):
            varB.append(varD)
        varC += 1

    def compare_asc(m: int, n: int) -> int:
        if m < n:
            return -1
        elif m > n:
            return 1
        else:
            return 0

    # Python's sort does not accept a cmp function since 3.x, so we emulate it using key.
    # The compare_asc only represents normal ascending order, so sort ascending directly.
    return sorted(varB)