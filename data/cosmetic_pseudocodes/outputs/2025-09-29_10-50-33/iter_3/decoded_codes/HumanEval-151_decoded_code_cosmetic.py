from typing import Sequence

def double_the_difference(collection_of_values: Sequence[int]) -> int:
    accumulator: int = 0
    pos: int = 0

    while pos < len(collection_of_values):
        element = collection_of_values[pos]

        if element > 0 and (element % 2) != 0:
            if '.' not in str(element):
                accumulator += element * element
        pos += 1

    return accumulator