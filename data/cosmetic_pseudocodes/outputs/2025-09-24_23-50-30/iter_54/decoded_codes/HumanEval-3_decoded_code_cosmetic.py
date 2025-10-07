from typing import Sequence

def below_zero(sequence: Sequence[int]) -> bool:
    accumulator: int = 0

    def iterate(index: int) -> bool:
        nonlocal accumulator
        if index == len(sequence):
            return False
        total = accumulator + sequence[index]
        if total < 0:
            return True
        accumulator = total
        return iterate(index + 1)

    return iterate(0)