from typing import Sequence, List

def sort_array(sequence: Sequence[int]) -> List[int]:
    initial_length: int = len(sequence)
    if initial_length != 0:
        first_element: int = sequence[0]
        last_element_index: int = initial_length - 1
        last_element: int = sequence[last_element_index]
        sum_ends: int = first_element + last_element
        even_sum_flag: bool = (sum_ends % 2 == 0)
        sorted_sequence: List[int] = sorted(sequence, reverse=even_sum_flag)
        return sorted_sequence
    else:
        return []