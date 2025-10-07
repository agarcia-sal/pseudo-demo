from typing import Sequence

def how_many_times(input_sequence: Sequence, search_sequence: Sequence) -> int:
    count_tracker: int = 0
    position: int = 0
    upper_limit: int = len(input_sequence) - len(search_sequence)
    while position <= upper_limit:
        extracted_segment = input_sequence[position : position + len(search_sequence)]
        if extracted_segment == search_sequence:
            count_tracker += 1
        position += 1
    return count_tracker