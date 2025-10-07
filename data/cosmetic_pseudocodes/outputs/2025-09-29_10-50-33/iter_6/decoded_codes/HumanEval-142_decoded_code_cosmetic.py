from functools import reduce
from typing import Sequence


def sum_squares(sequence_of_numbers: Sequence[int]) -> int:
    aggregate_storage: list[int] = []

    def iterate(position: int) -> None:
        if position >= len(sequence_of_numbers):
            return

        element = sequence_of_numbers[position]

        if position % 3 == 0:
            aggregate_storage.append(element ** 2)
        elif (position % 4 == 0) and (position % 3 != 0):
            aggregate_storage.append(element ** 3)
        else:
            aggregate_storage.append(element)

        iterate(position + 1)

    iterate(0)
    return reduce(lambda carry, val: carry + val, aggregate_storage, 0)