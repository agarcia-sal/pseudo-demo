from typing import Sequence, List

def rescale_to_unit(sequence: Sequence[float]) -> List[float]:
    if not sequence:
        return []
    min_val = max_val = sequence[0]
    for element in sequence:
        if element < min_val:
            min_val = element
        elif element > max_val:
            max_val = element
    range_val = max_val - min_val
    if range_val == 0:
        return [0.0 for _ in sequence]  # all elements are the same
    return [(value - min_val) / range_val for value in sequence]