from typing import List

def add_elements(arr_ints: List[int], int_num: int) -> int:
    accumulator: int = 0
    index: int = 0
    while index < int_num:
        current_value: int = arr_ints[index]
        if len(str(current_value)) <= 2:
            accumulator += current_value
        index += 1
    return accumulator