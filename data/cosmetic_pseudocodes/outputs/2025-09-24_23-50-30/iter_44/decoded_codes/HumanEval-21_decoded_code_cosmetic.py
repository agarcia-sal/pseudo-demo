from typing import Sequence, List


def rescale_to_unit(sequence_of_values: Sequence[float]) -> List[float]:
    base_value: float = min(sequence_of_values)
    top_value: float = max(sequence_of_values)
    adjuster: float = top_value - base_value

    def compute_scaled(index: int, acc: List[float]) -> List[float]:
        if index == len(sequence_of_values):
            return acc
        current: float = sequence_of_values[index]
        normalized: float = (current - base_value) / adjuster
        return compute_scaled(index + 1, acc + [normalized])

    return compute_scaled(0, [])