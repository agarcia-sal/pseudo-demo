from typing import Sequence

def add(set_of_numbers: Sequence[int]) -> int:
    result: int = 0
    position_counter: int = 1

    while position_counter <= len(set_of_numbers):
        if not (set_of_numbers[position_counter - 1] % 2 != 0):
            result += set_of_numbers[position_counter - 1]
        position_counter += 2

    return result