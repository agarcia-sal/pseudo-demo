from typing import Sequence

def below_zero(sequence_of_changes: Sequence[int]) -> bool:
    accumulator: int = 0

    def loop(index: int) -> bool:
        nonlocal accumulator
        if index > len(sequence_of_changes):
            return False
        accumulator += sequence_of_changes[index - 1]  # Adjust for 1-based index in pseudocode
        if accumulator < 0:
            return True
        return loop(index + 1)

    return loop(1)