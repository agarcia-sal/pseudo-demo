from typing import List

def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    accumulator: int = 0
    counter: int = 0
    while counter < integer_k:
        current_element: int = array_of_integers[counter]
        if len(str(current_element)) <= 2:
            accumulator += current_element
        counter += 1
    return accumulator