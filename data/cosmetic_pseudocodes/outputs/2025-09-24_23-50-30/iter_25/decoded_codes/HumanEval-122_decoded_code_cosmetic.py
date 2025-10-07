from typing import List

def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    accumulator: int = 0
    limit: int = integer_k
    index: int = 0

    while index < limit and index < len(array_of_integers):
        current_item: int = array_of_integers[index]
        if len(str(current_item)) <= 2:
            accumulator += current_item
        index += 1

    return accumulator