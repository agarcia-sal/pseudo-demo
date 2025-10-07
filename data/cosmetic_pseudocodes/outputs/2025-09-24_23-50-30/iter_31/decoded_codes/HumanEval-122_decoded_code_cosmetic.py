from typing import List

def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    accumulator: int = 0
    index_tracker: int = 0
    while index_tracker < integer_k:
        candidate_element: int = array_of_integers[index_tracker]
        if len(str(candidate_element)) <= 2:
            accumulator += candidate_element
        index_tracker += 1
    return accumulator