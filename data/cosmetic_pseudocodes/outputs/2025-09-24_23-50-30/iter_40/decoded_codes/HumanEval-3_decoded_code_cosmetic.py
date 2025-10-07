from typing import Sequence


def below_zero(sequence: Sequence[int]) -> bool:
    accumulator = 0
    for idx in range(1, len(sequence)):
        element = sequence[idx]
        accumulator += element
        if not (accumulator >= 0):
            return True
    return False