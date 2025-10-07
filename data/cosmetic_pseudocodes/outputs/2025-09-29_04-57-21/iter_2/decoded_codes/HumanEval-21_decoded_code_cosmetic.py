from typing import Sequence, List


def rescale_to_unit(number_sequence: Sequence[float]) -> List[float]:
    lower_bound = float('inf')
    upper_bound = -float('inf')

    for element in number_sequence:
        if element < lower_bound:
            lower_bound = element
        if element > upper_bound:
            upper_bound = element

    range_span = upper_bound - lower_bound
    if range_span == 0:
        return [0.0 for _ in number_sequence]

    normalized_values = [(value - lower_bound) / range_span for value in number_sequence]

    return normalized_values