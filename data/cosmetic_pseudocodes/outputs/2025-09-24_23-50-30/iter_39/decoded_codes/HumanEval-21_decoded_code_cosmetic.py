from typing import Sequence, List

def rescale_to_unit(sequence: Sequence[float]) -> List[float]:
    if not sequence:
        return []
    low_val = sequence[0]
    high_val = sequence[0]
    idx = 1
    while idx < len(sequence):
        val = sequence[idx]
        if val < low_val:
            low_val = val
        elif val > high_val:
            high_val = val
        idx += 1
    denominator = high_val - low_val
    if denominator == 0:
        # All elements equal; scale to 0.0 for all
        return [0.0] * len(sequence)
    result_list: List[float] = []
    pointer = 0
    while pointer < len(sequence):
        numerator = sequence[pointer] - low_val
        scaled_value = numerator / denominator
        result_list.append(scaled_value)
        pointer += 1
    return result_list