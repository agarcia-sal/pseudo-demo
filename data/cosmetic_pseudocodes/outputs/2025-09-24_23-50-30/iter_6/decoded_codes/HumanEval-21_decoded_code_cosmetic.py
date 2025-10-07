from typing import List

def rescale_to_unit(list_of_numbers: List[float]) -> List[float]:
    lower_bound: float = float('inf')
    upper_bound: float = float('-inf')
    idx: int = 0
    length: int = len(list_of_numbers)
    while idx < length:
        value = list_of_numbers[idx]
        if value < lower_bound:
            lower_bound = value
        if value > upper_bound:
            upper_bound = value
        idx += 1

    denominator: float = upper_bound - lower_bound
    output_list: List[float] = []
    pointer: int = 0
    while pointer < length:
        normalized_value = (list_of_numbers[pointer] - lower_bound) / denominator
        output_list.append(normalized_value)
        pointer += 1

    return output_list