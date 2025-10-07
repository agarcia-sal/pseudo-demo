from typing import List

def add_elements(input_list: List[int], count_limit: int) -> int:
    accumulator: int = 0
    current_index: int = 0
    while current_index < count_limit:
        current_value: int = input_list[current_index]
        str_value: str = str(current_value)
        if len(str_value) <= 2:
            accumulator += current_value
        current_index += 1
    return accumulator