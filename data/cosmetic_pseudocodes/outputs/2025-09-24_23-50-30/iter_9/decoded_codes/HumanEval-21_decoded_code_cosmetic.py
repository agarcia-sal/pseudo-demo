from typing import Sequence, List

def rescale_to_unit(sequence: Sequence[float]) -> List[float]:
    low_bound: float = float('inf')
    high_bound: float = float('-inf')

    for element in sequence:
        if element < low_bound:
            low_bound = element
        if element > high_bound:
            high_bound = element

    span = high_bound - low_bound
    if span == 0:
        # If all elements are equal, rescale to all zeros to avoid division by zero
        return [0.0 for _ in sequence]

    return [(value - low_bound) / span for value in sequence]