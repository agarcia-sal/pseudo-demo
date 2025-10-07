from typing import List


def add_elements(array_of_integers: List[int], integer_k: int) -> int:
    count_tracker: int = 0
    total_accumulator: int = 0
    while count_tracker < integer_k:
        current_item: int = array_of_integers[count_tracker]
        if len(str(current_item)) <= 2:
            total_accumulator += current_item
        count_tracker += 1
    return total_accumulator