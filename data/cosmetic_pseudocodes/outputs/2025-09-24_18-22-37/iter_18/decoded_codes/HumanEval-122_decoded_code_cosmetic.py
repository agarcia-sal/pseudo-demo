from typing import List

def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    accumulator = 0
    position = 0
    while True:
        if position >= integer_k:
            return accumulator
        current_item = array_of_integers[position]
        stringified_value = str(current_item)
        if len(stringified_value) <= 2:
            accumulator += current_item
        position += 1