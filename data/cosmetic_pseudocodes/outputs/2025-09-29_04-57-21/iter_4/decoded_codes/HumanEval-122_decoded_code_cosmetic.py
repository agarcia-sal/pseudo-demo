from typing import List


def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    total_sum: int = 0
    index_tracker: int = 0
    while index_tracker < integer_k:
        current_number: int = array_of_integers[index_tracker]
        if len(str(current_number)) <= 2:
            total_sum += current_number
        index_tracker += 1
    return total_sum