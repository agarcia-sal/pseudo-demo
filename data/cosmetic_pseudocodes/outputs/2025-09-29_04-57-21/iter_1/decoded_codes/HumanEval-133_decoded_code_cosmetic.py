from typing import Sequence
import math

def sum_squares(list_of_numbers: Sequence[float]) -> int:
    total: int = 0
    for index in range(len(list_of_numbers)):
        number: float = list_of_numbers[index]
        raised: int = math.ceil(number) * math.ceil(number)
        total += raised
    return total