from typing import List, Sequence


def rescale_to_unit(collection_of_values: Sequence[float]) -> List[float]:
    if not collection_of_values:
        return []
    lowest_value = float('inf')
    highest_value = float('-inf')
    for element_index in range(len(collection_of_values)):
        value = collection_of_values[element_index]
        if value < lowest_value:
            lowest_value = value
        if value > highest_value:
            highest_value = value
    range_diff = highest_value - lowest_value
    # Avoid division by zero when all values are equal
    if range_diff == 0:
        return [0.0] * len(collection_of_values)
    normalized_values = [0.0] * len(collection_of_values)
    for index_in_values in range(len(collection_of_values)):
        normalized_values[index_in_values] = (collection_of_values[index_in_values] - lowest_value) / range_diff
    return normalized_values