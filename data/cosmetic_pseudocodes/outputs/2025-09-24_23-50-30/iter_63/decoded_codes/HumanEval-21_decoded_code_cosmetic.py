from typing import Sequence, List

def rescale_to_unit(input_sequence: Sequence[float]) -> List[float]:
    if not input_sequence:
        return []

    min_val = input_sequence[0]
    max_val = input_sequence[0]

    for idx in range(1, len(input_sequence)):
        value = input_sequence[idx]
        if value < min_val:
            min_val = value
        elif value > max_val:
            max_val = value

    result_container: List[float] = []
    denominator = max_val - min_val

    for idx2 in range(len(input_sequence)):
        temp_diff = input_sequence[idx2] - min_val
        scaled_value = temp_diff / denominator if denominator != 0 else 0.0
        result_container.append(scaled_value)

    return result_container