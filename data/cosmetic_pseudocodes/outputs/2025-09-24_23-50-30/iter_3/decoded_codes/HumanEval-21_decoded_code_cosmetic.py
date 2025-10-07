from typing import List

def rescale_to_unit(list_of_numbers: List[float]) -> List[float]:
    min_val: float = list_of_numbers[0]
    max_val: float = list_of_numbers[0]

    for index in range(1, len(list_of_numbers)):
        if list_of_numbers[index] < min_val:
            min_val = list_of_numbers[index]
        if list_of_numbers[index] > max_val:
            max_val = list_of_numbers[index]

    range_len: float = max_val - min_val
    if range_len == 0:
        # If all values are equal, return zeros to avoid division by zero
        return [0.0 for _ in list_of_numbers]

    normalized_values: List[float] = [
        (list_of_numbers[i] - min_val) / range_len for i in range(len(list_of_numbers))
    ]
    return normalized_values