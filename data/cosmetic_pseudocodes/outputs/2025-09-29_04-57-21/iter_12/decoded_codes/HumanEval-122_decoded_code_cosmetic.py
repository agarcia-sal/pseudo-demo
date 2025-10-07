from typing import List

def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    aggregate_sum = 0
    position = 0
    while position < integer_k:
        current_val = array_of_integers[position]
        if len(str(current_val)) <= 2:  # Include numbers with length <= 2 digits
            aggregate_sum += current_val
        position += 1
    return aggregate_sum