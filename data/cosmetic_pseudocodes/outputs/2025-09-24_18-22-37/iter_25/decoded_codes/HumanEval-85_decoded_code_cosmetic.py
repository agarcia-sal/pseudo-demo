from typing import Sequence


def add(sequence: Sequence[int]) -> int:
    result_accumulator: int = 0
    position_tracker: int = 1
    length: int = len(sequence)
    while position_tracker <= length:
        current_element: int = sequence[position_tracker - 1]  # Adjusting 1-based index to 0-based
        if current_element % 2 == 0:
            result_accumulator += current_element
        position_tracker += 2
    return result_accumulator