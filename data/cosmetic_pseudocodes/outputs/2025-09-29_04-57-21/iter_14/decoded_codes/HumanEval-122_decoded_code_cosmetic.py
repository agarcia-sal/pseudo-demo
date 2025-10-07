from typing import List


def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    aggregate_sum = 0
    current_index = 0
    while current_index < integer_k:
        current_number = array_of_integers[current_index]
        if len(str(current_number)) <= 2:
            aggregate_sum += current_number
        current_index += 1
    return aggregate_sum