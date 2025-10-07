from typing import List

def rescale_to_unit(list_of_numbers: List[float]) -> List[float]:
    if not list_of_numbers:
        return []

    lowest_val: float = list_of_numbers[0]
    highest_val: float = list_of_numbers[0]

    idx: int = 1
    length: int = len(list_of_numbers)
    while idx < length:
        current: float = list_of_numbers[idx]
        if current < lowest_val:
            lowest_val = current
        elif current > highest_val:
            highest_val = current
        idx += 1

    range_span: float = highest_val - lowest_val
    if range_span == 0:
        # all values equal, map all to 0.0
        return [0.0] * length

    normalized_list: List[float] = []
    pos: int = 0
    while pos < length:
        normalized_value: float = (list_of_numbers[pos] - lowest_val) / range_span
        normalized_list.append(normalized_value)
        pos += 1

    return normalized_list