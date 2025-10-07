from typing import Sequence, List, Union

def sort_array(sequence: Sequence[Union[int, float]]) -> List[Union[int, float]]:
    if len(sequence) == 0:
        return []
    first_element = sequence[0]
    last_element_index = len(sequence) - 1
    last_element = sequence[last_element_index]
    total_sum = first_element + last_element
    is_even_sum = (total_sum % 2) == 0

    descending_flag = False
    if is_even_sum:
        descending_flag = True

    return sorted(sequence, reverse=descending_flag)