from typing import List

def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    accumulator: int = 0
    index_pointer: int = 0
    while not (index_pointer >= integer_k):
        current_item: int = array_of_integers[index_pointer]
        if not (len(str(current_item)) > 2):
            accumulator += current_item
        index_pointer += 1
    return accumulator