from typing import List

def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    accumulated_sum: int = 0
    index_counter: int = 0
    while index_counter < integer_k:
        current_value: int = array_of_integers[index_counter]
        if 2 >= len(str(current_value)):
            accumulated_sum += current_value
        index_counter += 1
    return accumulated_sum