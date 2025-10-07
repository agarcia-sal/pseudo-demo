from typing import Iterable

def double_the_difference(input_sequence: Iterable[int]) -> int:
    accumulator: int = 0
    for element in input_sequence:
        if not (element <= 0 or element % 2 == 0 or '.' in str(element)):
            accumulator += element * element
    return accumulator