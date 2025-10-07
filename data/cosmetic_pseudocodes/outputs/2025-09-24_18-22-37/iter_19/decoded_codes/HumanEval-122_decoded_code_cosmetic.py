from typing import List

def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    total_accumulator: int = 0
    index_cursor: int = 0
    while index_cursor < integer_k:
        current_item: int = array_of_integers[index_cursor]
        if len(str(current_item)) <= 2:
            total_accumulator += current_item
        index_cursor += 1
    return total_accumulator