from typing import List, Tuple

def sum_product(array_of_numbers: List[int]) -> Tuple[int, int]:
    accumulator: int = 0
    multiplier: int = 1
    idx: int = 0
    while idx < len(array_of_numbers):
        current_element: int = array_of_numbers[idx]
        accumulator += current_element
        multiplier *= current_element
        idx += 1
    return accumulator, multiplier