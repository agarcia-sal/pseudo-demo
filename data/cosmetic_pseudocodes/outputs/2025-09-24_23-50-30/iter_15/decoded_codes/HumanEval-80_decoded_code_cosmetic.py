from typing import Sequence

def is_happy(datum: Sequence[str]) -> bool:
    limit = len(datum) - 2
    if limit <= 0:
        return False
    for iterator in range(limit):
        first_char = datum[iterator]
        second_char = datum[iterator + 1]
        third_char = datum[iterator + 2]
        if not (first_char != second_char and second_char != third_char and first_char != third_char):
            return False
    return True