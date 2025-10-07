from typing import List

def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    total_accumulator: int = 0
    index_counter: int = 0

    while index_counter < integer_k:
        current_value: int = array_of_integers[index_counter]
        if not (len(str(current_value)) > 2):
            total_accumulator += current_value
        index_counter += 1

    return total_accumulator