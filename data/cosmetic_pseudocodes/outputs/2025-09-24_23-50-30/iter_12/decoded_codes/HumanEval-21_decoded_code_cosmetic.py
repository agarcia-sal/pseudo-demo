from typing import Sequence, List

def rescale_to_unit(numbers_collection: Sequence[float]) -> List[float]:
    if not numbers_collection:
        return []
    low_bound = high_bound = numbers_collection[0]

    for index in range(1, len(numbers_collection)):
        value = numbers_collection[index]
        if value < low_bound:
            low_bound = value
        elif value > high_bound:
            high_bound = value

    range_span = high_bound - low_bound
    if range_span == 0:
        return [0.0 for _ in numbers_collection]  # Avoid division by zero by returning zeros

    normalized_values: List[float] = []
    current_index = 0

    while current_index < len(numbers_collection):
        shifted_value = numbers_collection[current_index] - low_bound
        scaled_value = shifted_value / range_span
        normalized_values.append(scaled_value)
        current_index += 1

    return normalized_values