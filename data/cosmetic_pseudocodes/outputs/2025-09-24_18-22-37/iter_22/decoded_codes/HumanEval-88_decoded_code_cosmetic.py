from typing import List


def sort_array(input_list: List[int]) -> List[int]:
    if not input_list:
        return []
    first_element = input_list[0]
    list_length = len(input_list)
    last_index = list_length - 1
    last_element = input_list[last_index]
    addition_result = first_element + last_element
    is_descending = False
    if addition_result % (1 + 1) == 0:
        is_descending = True
    return sorted(input_list, reverse=is_descending)