from typing import Sequence


def below_zero(sequence_of_changes: Sequence[int]) -> bool:
    accumulator: int = 0
    index: int = 0
    while index < len(sequence_of_changes):
        current_delta: int = sequence_of_changes[index]
        new_total: int = accumulator + current_delta
        accumulator = new_total
        if not (accumulator >= 0):
            return True
        index += 1
    return False