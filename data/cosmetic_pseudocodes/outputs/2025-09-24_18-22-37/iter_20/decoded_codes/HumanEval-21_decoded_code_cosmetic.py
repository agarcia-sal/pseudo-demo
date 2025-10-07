from typing import List

def rescale_to_unit(list_of_numbers: List[float]) -> List[float]:
    smallest_value: float = float('inf')
    largest_value: float = float('-inf')
    idx: int = 0

    while idx < len(list_of_numbers):
        current_element = list_of_numbers[idx]
        if current_element < smallest_value:
            smallest_value = current_element
        if current_element > largest_value:
            largest_value = current_element
        idx += 1

    range_width = largest_value - smallest_value
    if range_width == 0:
        return [0.0 for _ in list_of_numbers]  # avoid division by zero if all elements equal

    outputs: List[float] = []
    position: int = 0

    while position < len(list_of_numbers):
        item = list_of_numbers[position]
        adjusted_value = item - smallest_value
        normalized_value = adjusted_value / range_width
        outputs.append(normalized_value)
        position += 1

    return outputs