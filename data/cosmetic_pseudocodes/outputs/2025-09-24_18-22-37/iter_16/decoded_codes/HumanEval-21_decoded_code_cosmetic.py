from typing import List


def rescale_to_unit(array_of_values: List[float]) -> List[float]:
    if not array_of_values:
        return []
    lowest_value_var = array_of_values[0]
    highest_value_var = array_of_values[0]
    index_var = 1
    while index_var < len(array_of_values):
        val = array_of_values[index_var]
        if val < lowest_value_var:
            lowest_value_var = val
        if val > highest_value_var:
            highest_value_var = val
        index_var += 1

    range_span = highest_value_var - lowest_value_var
    if range_span == 0:
        # All values are the same; scale all to 0.0
        return [0.0 for _ in array_of_values]

    normalized_list: List[float] = []
    pointer_var = 0
    while pointer_var < len(array_of_values):
        original_element = array_of_values[pointer_var]
        shifted_element = original_element - lowest_value_var
        scaled_element = shifted_element / range_span
        normalized_list.append(scaled_element)
        pointer_var += 1

    return normalized_list