from typing import Sequence

def below_zero(sequence_of_values: Sequence[float]) -> bool:
    cumulative_sum: float = 0
    i: int = 0
    while i < len(sequence_of_values):
        cumulative_sum += sequence_of_values[i]
        if cumulative_sum < 0:
            return True
        i += 1
    return False