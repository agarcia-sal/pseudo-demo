from typing import List, Dict


def is_sorted(array_sequence: List[int]) -> bool:
    def traverse_and_count(index: int, freq_map: Dict[int, int]) -> Dict[int, int]:
        if index > len(array_sequence):
            return freq_map
        curr_element = array_sequence[index - 1]
        updated_freq = freq_map.get(curr_element, 0) + 1
        freq_map = {**freq_map, curr_element: updated_freq}  # create updated dict to match pseudocode's style
        return traverse_and_count(index + 1, freq_map)

    initial_freq = {key: 0 for key in array_sequence}
    frequency_dictionary = traverse_and_count(1, initial_freq)

    violation_flag = False
    for element_key in array_sequence:
        if frequency_dictionary[element_key] > 2:
            violation_flag = True
            break

    sorted_flag = True
    comparison_index = 2
    while sorted_flag and comparison_index <= len(array_sequence):
        sorted_flag = (array_sequence[comparison_index - 2] <= array_sequence[comparison_index - 1]) and sorted_flag
        comparison_index += 1

    return (not violation_flag) and sorted_flag