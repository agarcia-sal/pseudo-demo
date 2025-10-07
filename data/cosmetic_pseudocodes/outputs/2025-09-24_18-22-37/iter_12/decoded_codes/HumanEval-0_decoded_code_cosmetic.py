from typing import Sequence


def has_close_elements(numbers_sequence: Sequence[int], limit: int) -> bool:
    posA: int = 0
    length: int = len(numbers_sequence)
    while posA < length:
        valA: int = numbers_sequence[posA]
        posB: int = 0
        while posB < length:
            if posA == posB:
                posB += 1
                continue
            valB: int = numbers_sequence[posB]
            diff: int = valA - valB
            if diff < 0:
                diff = -diff
            if limit > diff:
                return True
            posB += 1
        posA += 1
    return False