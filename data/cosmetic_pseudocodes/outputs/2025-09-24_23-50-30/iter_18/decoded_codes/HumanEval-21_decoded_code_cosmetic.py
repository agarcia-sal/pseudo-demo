from typing import List

def rescale_to_unit(list_of_numbers: List[float]) -> List[float]:
    if not list_of_numbers:
        return []

    smallest_value: float = list_of_numbers[0]
    largest_value: float = list_of_numbers[0]
    index: int = 1

    while index < len(list_of_numbers):
        value = list_of_numbers[index]
        if value < smallest_value:
            smallest_value = value
        if value > largest_value:
            largest_value = value
        index += 1

    range_span: float = largest_value - smallest_value
    if range_span == 0:
        # All values are the same; return zeros to avoid division by zero
        return [0.0] * len(list_of_numbers)

    output_array: List[float] = []
    index = 0
    while index < len(list_of_numbers):
        normalized_value = (list_of_numbers[index] - smallest_value) / range_span
        output_array.append(normalized_value)
        index += 1

    return output_array