from typing import List


def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    accumulator: int = 0
    limit: int = integer_k - 1
    index: int = 0
    while index <= limit:
        current_val: int = array_of_integers[index]
        if len(str(current_val)) <= 2:
            accumulator += current_val
        index += 1
    return accumulator