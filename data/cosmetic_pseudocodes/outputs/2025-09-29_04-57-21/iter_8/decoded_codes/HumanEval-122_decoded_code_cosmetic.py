from typing import List


def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    accumulator = 0
    counter = 0
    while counter < integer_k:
        current_value = array_of_integers[counter]
        if not (len(str(current_value)) > 2):
            accumulator += current_value
        counter += 1
    return accumulator