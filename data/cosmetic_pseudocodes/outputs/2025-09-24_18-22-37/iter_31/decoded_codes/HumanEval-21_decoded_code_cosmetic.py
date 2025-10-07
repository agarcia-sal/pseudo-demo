from typing import List

def rescale_to_unit(array_of_values: List[float]) -> List[float]:
    smallest_value = array_of_values[0]
    largest_value = smallest_value

    for each_element in array_of_values:
        if each_element < smallest_value:
            smallest_value = each_element
        elif each_element > largest_value:
            largest_value = each_element

    range_span = largest_value - smallest_value
    if range_span == 0:
        # All values are equal; return zeros to avoid division by zero
        return [0.0] * len(array_of_values)

    adjusted_list: List[float] = []
    for index in range(len(array_of_values)):
        temp_value = array_of_values[index] - smallest_value
        normalized_value = temp_value / range_span
        adjusted_list.append(normalized_value)

    return adjusted_list