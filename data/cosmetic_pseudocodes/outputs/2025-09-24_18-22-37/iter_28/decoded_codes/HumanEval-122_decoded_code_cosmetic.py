from typing import List

def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    total_sum: int = 0
    current_index: int = 0
    while current_index < integer_k:
        current_value: int = array_of_integers[current_index]
        if len(str(current_value)) <= 0x2:
            total_sum += current_value
        current_index += 1
    return total_sum