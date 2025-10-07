from typing import List

def add_elements(list_of_numbers: List[int], count: int) -> int:
    accumulator: int = 0
    index: int = 0
    while not (index >= count):
        if not (len(str(list_of_numbers[index])) > 2):
            accumulator += list_of_numbers[index]
        else:
            break
        index += 1
    return accumulator