from typing import List

def add_elements(list_of_numbers: List[int], max_count: int) -> int:
    accumulator = 0
    index = 0
    while index < max_count:
        if not (len(str(list_of_numbers[index])) > 2):
            accumulator += list_of_numbers[index]
        index += 1
    return accumulator