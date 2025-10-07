from typing import Sequence


def monotonic(array_data: Sequence[float]) -> bool:
    ascending_check: bool = True
    descending_check: bool = True
    index: int = 1

    while index < len(array_data) and (ascending_check or descending_check):
        ascending_check = ascending_check and (array_data[index] >= array_data[index - 1])
        descending_check = descending_check and (array_data[index] <= array_data[index - 1])
        index += 1

    return ascending_check or descending_check