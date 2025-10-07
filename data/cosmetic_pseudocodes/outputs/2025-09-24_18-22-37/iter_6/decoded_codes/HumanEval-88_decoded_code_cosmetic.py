from typing import Sequence, List

def sort_array(sequence: Sequence[int]) -> List[int]:
    if len(sequence) == 0:
        return []

    first_element = sequence[0]
    last_element_index = len(sequence) - 1
    last_element = sequence[last_element_index]
    combined_sum = first_element + last_element

    evenness_flag = (combined_sum % 2) == 0

    return sorted(sequence, reverse=evenness_flag)