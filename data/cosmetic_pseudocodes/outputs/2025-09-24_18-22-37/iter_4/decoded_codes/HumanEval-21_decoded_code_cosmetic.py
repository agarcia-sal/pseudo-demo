from typing import Sequence, List

def rescale_to_unit(number_sequence: Sequence[float]) -> List[float]:
    if not number_sequence:
        return []
    min_val: float = number_sequence[0]
    max_val: float = number_sequence[0]
    index: int = 1
    while index < len(number_sequence):
        val = number_sequence[index]
        if val < min_val:
            min_val = val
        elif val > max_val:
            max_val = val
        index += 1
    denominator = max_val - min_val
    scaled_list: List[float] = []
    pointer: int = 0
    while pointer < len(number_sequence):
        if denominator == 0:
            normalized_value = 0.0  # all values are the same
        else:
            normalized_value = (number_sequence[pointer] - min_val) / denominator
        scaled_list.append(normalized_value)
        pointer += 1
    return scaled_list