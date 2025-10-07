from typing import Sequence, List

def rescale_to_unit(data_sequence: Sequence[float]) -> List[float]:
    if not data_sequence:
        return []

    lower_bound: float = data_sequence[0]
    upper_bound: float = data_sequence[0]

    for element in data_sequence[1:]:
        if element < lower_bound:
            lower_bound = element
        elif element > upper_bound:
            upper_bound = element

    delta = upper_bound - lower_bound
    if delta == 0:
        # All elements are equal; return zeros to avoid division by zero
        return [0.0] * len(data_sequence)

    output_sequence: List[float] = []
    index = 0

    while index < len(data_sequence):
        normalized_value = (data_sequence[index] - lower_bound) / delta
        output_sequence.append(normalized_value)
        index += 1

    return output_sequence