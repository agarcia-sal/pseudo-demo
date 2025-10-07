from typing import Sequence, List

def rescale_to_unit(input_sequence: Sequence[float]) -> List[float]:
    if not input_sequence:
        return []

    lower_bound: float = input_sequence[0]
    upper_bound: float = input_sequence[0]

    for element_index in range(1, len(input_sequence)):
        value = input_sequence[element_index]
        if value < lower_bound:
            lower_bound = value
        elif value > upper_bound:
            upper_bound = value

    range_span = upper_bound - lower_bound
    if range_span == 0:
        # All elements are equal; map all to 0.0
        return [0.0] * len(input_sequence)

    normalized_result: List[float] = []
    current_index = 0
    length = len(input_sequence)

    while current_index < length:
        normalized_value = (input_sequence[current_index] - lower_bound) / range_span
        normalized_result.append(normalized_value)
        current_index += 1

    return normalized_result