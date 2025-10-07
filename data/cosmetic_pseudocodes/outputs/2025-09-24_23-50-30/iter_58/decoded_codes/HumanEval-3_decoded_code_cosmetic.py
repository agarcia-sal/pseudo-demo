from typing import Sequence


def below_zero(delta_sequence: Sequence[int]) -> bool:
    accumulator: int = 0

    def checker(index: int) -> bool:
        nonlocal accumulator
        if index == len(delta_sequence):
            return False
        accumulator += delta_sequence[index]
        if accumulator < 0:
            return True
        return checker(index + 1)

    return checker(0)