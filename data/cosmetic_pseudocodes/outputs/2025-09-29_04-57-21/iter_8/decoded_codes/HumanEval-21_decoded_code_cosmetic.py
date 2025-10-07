from typing import List

def rescale_to_unit(list_of_numbers: List[float]) -> List[float]:
    smallest_value: float = float('inf')
    largest_value: float = float('-inf')

    iterator = iter(list_of_numbers)
    for current_val in iterator:
        if current_val < smallest_value:
            smallest_value = current_val
        if current_val > largest_value:
            largest_value = current_val

    range_span = largest_value - smallest_value
    if range_span == 0:
        # Avoid division by zero: if all values are equal, map them all to 0.0
        return [0.0 for _ in list_of_numbers]

    result_collection: List[float] = []
    index = 0
    while index < len(list_of_numbers):
        original_val = list_of_numbers[index]
        normalized_val = (original_val - smallest_value) / range_span
        result_collection.append(normalized_val)
        index += 1

    return result_collection