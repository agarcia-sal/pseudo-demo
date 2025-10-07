from typing import Sequence

def below_zero(sequence_of_changes: Sequence[int]) -> bool:
    accumulator = 0

    def examine(index: int) -> bool:
        nonlocal accumulator
        if index == len(sequence_of_changes):
            return False
        accumulator += sequence_of_changes[index]
        return accumulator < 0 or examine(index + 1)

    return examine(0)