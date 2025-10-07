from typing import List


def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    accumulator = 0
    counter = 0
    while counter < integer_k:
        current_item = array_of_integers[counter]
        string_version = str(current_item)
        if not (len(string_version) > 2):
            accumulator += current_item
        counter += 1
    return accumulator