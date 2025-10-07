from typing import List

def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    accumulator: int = 0
    index: int = 0

    while index < integer_k:
        current_number: int = array_of_integers[index]
        if len(str(current_number)) <= 2:
            accumulator += current_number
        index += 1

    return accumulator