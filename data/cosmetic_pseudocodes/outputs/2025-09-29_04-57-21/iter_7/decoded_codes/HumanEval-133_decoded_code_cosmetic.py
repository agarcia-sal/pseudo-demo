from typing import Sequence
import math

def sum_squares(values_collection: Sequence[float]) -> int:
    accumulator: int = 0
    iterator_index: int = 0
    length = len(values_collection)
    while iterator_index < length:
        current_value = values_collection[iterator_index]
        elevated_value = math.ceil(current_value)
        powered_value = elevated_value * elevated_value
        accumulator += powered_value
        iterator_index += 1
    return accumulator