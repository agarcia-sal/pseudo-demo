from typing import Sequence, TypeVar, Optional

T = TypeVar('T')


def next_smallest(input_sequence: Sequence[T]) -> Optional[T]:
    sequence_map: dict[T, bool] = {}
    for element in input_sequence:
        sequence_map[element] = True

    distinct_elements = list(sequence_map.keys())
    sorted_elements = distinct_elements[:]
    index_counter = 0
    while index_counter < len(sorted_elements) - 1:
        inner_counter = 0
        while inner_counter < len(sorted_elements) - index_counter - 1:
            if sorted_elements[inner_counter] > sorted_elements[inner_counter + 1]:
                temp_val = sorted_elements[inner_counter]
                sorted_elements[inner_counter] = sorted_elements[inner_counter + 1]
                sorted_elements[inner_counter + 1] = temp_val
            inner_counter += 1
        index_counter += 1

    if len(sorted_elements) - 2 < 0:
        return None

    return sorted_elements[1]