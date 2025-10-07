from typing import Sequence

def sum_squares(values: Sequence[int]) -> int:
    accumulator: list[int] = []
    position: int = 0
    while position < len(values):
        if position % 3 == 0:
            accumulator.append(values[position] ** 2)
        elif position % 4 == 0 and position % 3 != 0:
            accumulator.append(values[position] ** 3)
        else:
            accumulator.append(values[position])
        position += 1
    total: int = 0
    for item in accumulator:
        total += item
    return total