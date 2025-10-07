from typing import Sequence

def add(sequence_of_numbers: Sequence[int]) -> int:
    accumulator: int = 0
    cursor: int = 1
    count_limit: int = len(sequence_of_numbers)
    while cursor <= count_limit:
        temp_element: int = sequence_of_numbers[cursor - 1]  # 1-based to 0-based index
        is_even_flag: bool = (temp_element % 2) == 0
        if is_even_flag:
            accumulator += temp_element
        cursor += 2
    return accumulator