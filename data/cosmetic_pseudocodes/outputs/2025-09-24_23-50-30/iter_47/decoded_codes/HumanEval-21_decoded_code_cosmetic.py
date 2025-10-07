from typing import Sequence, List

def rescale_to_unit(original_sequence: Sequence[float]) -> List[float]:
    if not original_sequence:
        return []
    smallest_value: float = float('inf')
    largest_value: float = float('-inf')
    for value in original_sequence:
        if value < smallest_value:
            smallest_value = value
        if value > largest_value:
            largest_value = value
    interval_length = largest_value - smallest_value
    if interval_length == 0:
        return [0.0 for _ in original_sequence]
    return [(value - smallest_value) / interval_length for value in original_sequence]