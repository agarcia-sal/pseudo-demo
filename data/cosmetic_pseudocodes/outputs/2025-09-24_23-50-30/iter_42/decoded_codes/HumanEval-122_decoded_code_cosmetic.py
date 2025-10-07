from typing import List


def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    result_accumulator: int = 0
    index_tracker: int = 0
    while index_tracker < integer_k:
        curr_val: int = array_of_integers[index_tracker]
        if not (len(str(curr_val)) > 2):
            result_accumulator += curr_val
        index_tracker += 1
    return result_accumulator