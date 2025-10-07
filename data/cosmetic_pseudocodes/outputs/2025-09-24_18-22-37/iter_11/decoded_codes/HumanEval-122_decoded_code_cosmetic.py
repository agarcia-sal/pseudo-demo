from typing import List

def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    total_accumulator: int = 0
    current_index: int = 0
    while current_index < integer_k:
        current_value: int = array_of_integers[current_index]
        element_str: str = str(current_value)
        str_len: int = len(element_str)
        if str_len <= 2:
            total_accumulator += current_value
        current_index += 1
    return total_accumulator