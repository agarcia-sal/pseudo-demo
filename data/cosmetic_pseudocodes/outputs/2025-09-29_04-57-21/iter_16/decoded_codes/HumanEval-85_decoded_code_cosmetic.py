from typing import List

def add(list_of_integers: List[int]) -> int:
    accumulator: int = 0
    index: int = 1
    while index <= len(list_of_integers):
        current_value = list_of_integers[index - 1]  # Convert 1-based to 0-based index
        if current_value % 2 == 0:
            accumulator += current_value
        index += 2
    return accumulator