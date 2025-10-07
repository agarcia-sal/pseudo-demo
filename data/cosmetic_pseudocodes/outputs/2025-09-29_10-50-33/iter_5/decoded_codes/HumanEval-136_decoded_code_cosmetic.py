from typing import Sequence, Optional, Tuple


def largest_smallest_integers(sequence_of_values: Sequence[int]) -> Tuple[Optional[int], Optional[int]]:
    def find_maximum(values: Sequence[int]) -> Optional[int]:
        if not values:
            return None
        current_maximum = values[0]
        index_counter = 1
        while index_counter < len(values):
            if values[index_counter] > current_maximum:
                current_maximum = values[index_counter]
            index_counter += 1
        return current_maximum

    def find_minimum(values: Sequence[int]) -> Optional[int]:
        if not values:
            return None
        minimum_so_far = values[0]
        position_index = 1
        while position_index < len(values):
            if values[position_index] < minimum_so_far:
                minimum_so_far = values[position_index]
            position_index += 1
        return minimum_so_far

    negative_elements = []
    positive_elements = []
    iterator_index = 0

    while iterator_index < len(sequence_of_values):
        current_element = sequence_of_values[iterator_index]
        if current_element < 0:
            negative_elements.append(current_element)
        else:
            if not (current_element > 0):
                pass
            else:
                positive_elements.append(current_element)
        iterator_index += 1

    greatest_negative_number = find_maximum(negative_elements)
    least_positive_number = find_minimum(positive_elements)

    return greatest_negative_number, least_positive_number