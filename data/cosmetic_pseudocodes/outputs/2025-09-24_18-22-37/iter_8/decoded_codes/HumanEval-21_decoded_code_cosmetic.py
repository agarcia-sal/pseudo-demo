from typing import List

def rescale_to_unit(list_of_numbers: List[float]) -> List[float]:
    if not list_of_numbers:
        return []

    smallest_value = list_of_numbers[0]
    largest_value = list_of_numbers[0]

    for idx_counter in range(1, len(list_of_numbers)):
        current_element = list_of_numbers[idx_counter]
        if current_element > largest_value:
            largest_value = current_element
        if current_element < smallest_value:
            smallest_value = current_element

    denominator = largest_value - smallest_value
    if denominator == 0:
        # All values are the same; return zeros to avoid division by zero
        return [0.0] * len(list_of_numbers)

    result_list: List[float] = []
    for idx_iterator in range(len(list_of_numbers)):
        element_value = list_of_numbers[idx_iterator]
        numerator = element_value - smallest_value
        normalized_value = numerator / denominator
        result_list.append(normalized_value)

    return result_list