from typing import List


def add_elements(list_of_numbers: List[int], number_m: int) -> int:
    accumulator = 0
    index_tracker = 0
    while index_tracker < number_m:
        current_item = list_of_numbers[index_tracker]
        if not (len(str(current_item)) > 2):
            accumulator += current_item
        index_tracker += 1
    return accumulator