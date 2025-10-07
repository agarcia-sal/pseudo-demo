from typing import List

def rescale_to_unit(list_of_numbers: List[float]) -> List[float]:
    if not list_of_numbers:
        return []

    smallest_val: float = list_of_numbers[0]
    largest_val: float = list_of_numbers[0]
    idx: int = 1

    while idx < len(list_of_numbers):
        current = list_of_numbers[idx]
        if current < smallest_val:
            smallest_val = current
        elif current > largest_val:
            largest_val = current
        idx += 1

    divisor = largest_val - smallest_val
    if divisor == 0:
        # Avoid division by zero when all elements are equal; return zeros
        return [0.0 for _ in list_of_numbers]

    normalized_list: List[float] = []
    pos: int = 0
    while pos < len(list_of_numbers):
        current_element = list_of_numbers[pos]
        difference = current_element - smallest_val
        normalized_value = difference / divisor
        normalized_list.append(normalized_value)
        pos += 1

    return normalized_list