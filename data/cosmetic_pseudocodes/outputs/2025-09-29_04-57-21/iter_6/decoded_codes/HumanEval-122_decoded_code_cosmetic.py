from typing import List


def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    total_sum = 0
    index_counter = 0
    while index_counter < integer_k:
        current_value = array_of_integers[index_counter]
        if len(str(current_value)) <= 2:
            total_sum += current_value
        index_counter += 1
    return total_sum