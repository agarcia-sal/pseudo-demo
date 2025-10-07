from typing import Sequence, List

def sort_array(input_sequence: Sequence[int]) -> List[int]:
    if not input_sequence:
        return []
    initial_plus_terminal = input_sequence[0] + input_sequence[-1]
    is_descending = (initial_plus_terminal % 2 == 0)
    sorted_sequence = sorted(input_sequence)
    return sorted_sequence[::-1] if is_descending else sorted_sequence