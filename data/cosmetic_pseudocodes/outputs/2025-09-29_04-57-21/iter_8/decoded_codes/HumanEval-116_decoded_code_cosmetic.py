from typing import List, Dict


def sort_array(array_of_integers: List[int]) -> List[int]:
    sorted_temp_list: List[int] = list(array_of_integers)
    index_counter: int = 0

    # Selection sort implementation
    while index_counter < len(sorted_temp_list):
        min_idx: int = index_counter
        inner_counter: int = index_counter + 1
        while inner_counter < len(sorted_temp_list):
            if sorted_temp_list[inner_counter] < sorted_temp_list[min_idx]:
                min_idx = inner_counter
            inner_counter += 1

        if min_idx != index_counter:
            sorted_temp_list[index_counter], sorted_temp_list[min_idx] = (
                sorted_temp_list[min_idx],
                sorted_temp_list[index_counter],
            )
        index_counter += 1

    grouping_dictionary: Dict[int, List[int]] = {}

    for number in sorted_temp_list:
        binary_form: str = bin(number)
        count_ones: int = sum(1 for ch in binary_form[2:] if ch == "1")

        if count_ones not in grouping_dictionary:
            grouping_dictionary[count_ones] = []
        grouping_dictionary[count_ones].append(number)

    result_list: List[int] = []
    key_values: List[int] = list(grouping_dictionary.keys())

    # Bubble sort implementation on keys
    i: int = 0
    while i < len(key_values) - 1:
        if key_values[i] > key_values[i + 1]:
            key_values[i], key_values[i + 1] = key_values[i + 1], key_values[i]
            i = -1
        i += 1

    for key in key_values:
        result_list.extend(grouping_dictionary[key])

    return result_list