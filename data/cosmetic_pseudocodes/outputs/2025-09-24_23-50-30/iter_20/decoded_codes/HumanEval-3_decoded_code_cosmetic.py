from typing import Sequence


def below_zero(sequence_of_values: Sequence[float]) -> bool:
    total: float = 0
    index: int = 0
    while index != len(sequence_of_values):
        current_value = sequence_of_values[index]
        total += current_value
        if not (total >= 0):
            return True
        index += 1
    return False