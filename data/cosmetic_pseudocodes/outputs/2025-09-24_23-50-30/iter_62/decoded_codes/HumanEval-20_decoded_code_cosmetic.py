from typing import Sequence, Optional, Tuple


def find_closest_elements(sequence_of_values: Sequence[float]) -> Optional[Tuple[float, float]]:
    def helper(i: int, j: int, current_best: Optional[Tuple[float, float]], current_min: Optional[float]) -> Optional[Tuple[float, float]]:
        if i == len(sequence_of_values):
            return current_best
        if j == len(sequence_of_values):
            return helper(i + 1, 0, current_best, current_min)
        val_i = sequence_of_values[i]
        val_j = sequence_of_values[j]
        if i != j:
            diff = abs(val_i - val_j)
            updated_min = diff if current_min is None else min(diff, current_min)
            updated_best = (tuple(sorted((val_i, val_j))) if current_min is None or diff < current_min else current_best)
            return helper(i, j + 1, updated_best, updated_min)
        return helper(i, j + 1, current_best, current_min)

    return helper(0, 0, None, None)