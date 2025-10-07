from typing import Sequence, List

def rescale_to_unit(sequence: Sequence[float]) -> List[float]:
    lower_bound: float = sequence[0]
    upper_bound: float = sequence[0]

    for element in sequence:
        if element < lower_bound:
            lower_bound = element
        elif element > upper_bound:
            upper_bound = element

    scale: float = upper_bound - lower_bound
    # Avoid division by zero if all values are equal
    if scale == 0:
        return [0.0 for _ in sequence]

    adjusted_values: List[float] = [
        (sequence[index] - lower_bound) / scale for index in range(len(sequence))
    ]

    return adjusted_values