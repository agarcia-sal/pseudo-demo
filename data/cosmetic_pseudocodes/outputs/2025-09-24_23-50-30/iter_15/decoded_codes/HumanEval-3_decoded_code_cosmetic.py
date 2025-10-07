from typing import Sequence

def below_zero(operations_sequence: Sequence[int]) -> bool:
    accumulator: int = 0
    idx: int = 0

    while idx < len(operations_sequence):
        accumulator += operations_sequence[idx]
        if accumulator < 0:
            return True
        idx += 1

    return False