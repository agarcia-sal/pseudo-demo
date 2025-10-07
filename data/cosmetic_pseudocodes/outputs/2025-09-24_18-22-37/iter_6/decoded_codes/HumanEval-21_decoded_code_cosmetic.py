from typing import List

def rescale_to_unit(list_of_numbers: List[float]) -> List[float]:
    idx: int = 0
    length: int = len(list_of_numbers)
    current_min: float = list_of_numbers[0]
    current_max: float = list_of_numbers[0]

    # Find minimum and maximum values
    while idx < length:
        if list_of_numbers[idx] < current_min:
            current_min = list_of_numbers[idx]
        elif list_of_numbers[idx] > current_max:
            current_max = list_of_numbers[idx]
        idx += 1

    output_list: List[float] = []
    pos: int = 0
    range_val: float = current_max - current_min

    # Avoid division by zero if all values are equal
    if range_val == 0:
        return [0.0] * length

    # Normalize each value to [0,1]
    while pos < length:
        difference_num: float = list_of_numbers[pos] - current_min
        normalized_val: float = difference_num / range_val
        output_list.append(normalized_val)
        pos += 1

    return output_list