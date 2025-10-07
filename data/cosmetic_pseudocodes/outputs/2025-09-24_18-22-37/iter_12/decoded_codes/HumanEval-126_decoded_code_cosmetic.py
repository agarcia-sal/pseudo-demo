from typing import Sequence, TypeVar

T = TypeVar('T')

def is_sorted(sequence_elements: Sequence[T]) -> bool:
    frequency_map: dict[T, int] = {}
    for index_var in range(len(sequence_elements)):
        item_key = sequence_elements[index_var]
        if item_key not in frequency_map:
            frequency_map[item_key] = 0
        count_before = frequency_map[item_key]
        count_after = count_before + 1
        frequency_map[item_key] = count_after

    violation_flag = False
    for element_key in frequency_map.keys():
        occurrence_value = frequency_map[element_key]
        if occurrence_value > 2:
            violation_flag = True
            break
    if violation_flag:
        return False

    position_var = 1
    flag_sorted = True
    while position_var < len(sequence_elements):
        previous_element = sequence_elements[position_var - 1]
        current_element = sequence_elements[position_var]
        if previous_element > current_element:
            flag_sorted = False
            break
        position_var += 1

    if flag_sorted:
        return True
    return False