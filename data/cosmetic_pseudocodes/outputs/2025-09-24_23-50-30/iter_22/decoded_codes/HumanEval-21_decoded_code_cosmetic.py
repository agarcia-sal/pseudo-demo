from typing import Sequence, List

def rescale_to_unit(sequence_of_values: Sequence[float]) -> List[float]:
    min_val: float = float('inf')
    max_val: float = float('-inf')
    for each_val in sequence_of_values:
        if each_val < min_val:
            min_val = each_val
        if each_val > max_val:
            max_val = each_val
    range_span = max_val - min_val
    if range_span == 0.0:
        # All values are the same; return zeros accordingly
        return [0.0 for _ in sequence_of_values]
    normalized_values: List[float] = []
    for val in sequence_of_values:
        adjusted_val = val - min_val
        scaled_val = adjusted_val / range_span
        normalized_values.append(scaled_val)
    return normalized_values