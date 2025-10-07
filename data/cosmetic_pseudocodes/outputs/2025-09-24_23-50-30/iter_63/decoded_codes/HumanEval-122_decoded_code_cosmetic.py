from typing import List

def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    sum_counter: int = 0
    index_tracker: int = 1
    while index_tracker <= integer_k and index_tracker <= len(array_of_integers):
        current_item: int = array_of_integers[index_tracker]
        if not (len(str(current_item)) > 2):
            sum_counter += current_item
        index_tracker += 1
    return sum_counter