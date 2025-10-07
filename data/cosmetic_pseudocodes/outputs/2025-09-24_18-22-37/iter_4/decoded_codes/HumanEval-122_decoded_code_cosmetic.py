from typing import List


def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    total_sum = 0
    index = 0
    while index < integer_k:
        current_val = array_of_integers[index]
        if len(str(current_val)) <= 2:
            total_sum += current_val
        index += 1
    return total_sum