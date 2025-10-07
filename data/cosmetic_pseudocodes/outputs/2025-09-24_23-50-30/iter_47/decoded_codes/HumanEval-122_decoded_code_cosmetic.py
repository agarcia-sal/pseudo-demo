from typing import List


def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    accumulator = 0
    index_counter = 1
    while index_counter <= integer_k and index_counter <= len(array_of_integers):
        active_value = array_of_integers[index_counter]
        if len(str(active_value)) <= 2:
            accumulator += active_value
        index_counter += 1
    return accumulator