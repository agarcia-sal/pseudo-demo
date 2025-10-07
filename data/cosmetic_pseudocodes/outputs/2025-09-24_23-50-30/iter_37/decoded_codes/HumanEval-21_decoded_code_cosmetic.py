from typing import Sequence, List

def rescale_to_unit(sequence_values: Sequence[float]) -> List[float]:
    low_val: float = sequence_values[0]
    high_val: float = sequence_values[0]

    for element in sequence_values:
        if element < low_val:
            low_val = element
        elif element > high_val:
            high_val = element

    range_val = high_val - low_val
    if range_val == 0:
        return [0.0 for _ in sequence_values]

    return [(item - low_val) / range_val for item in sequence_values]