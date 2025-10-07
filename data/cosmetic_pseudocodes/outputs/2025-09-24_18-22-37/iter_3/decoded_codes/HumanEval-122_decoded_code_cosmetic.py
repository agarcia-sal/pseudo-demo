from typing import List

def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    total_sum: int = 0
    index: int = 0
    while index < integer_k:
        current_value: int = array_of_integers[index]
        if len(str(current_value)) <= 2:
            total_sum += current_value
        index += 1
    return total_sum