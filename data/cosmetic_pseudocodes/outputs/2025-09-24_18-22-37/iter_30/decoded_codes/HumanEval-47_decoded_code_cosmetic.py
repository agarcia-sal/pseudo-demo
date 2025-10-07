from typing import Sequence, TypeVar, Union

T = TypeVar('T', bound=Union[int, float])

def median(items: Sequence[T]) -> float:
    sorted_items = sorted(items)
    length_of_sorted = len(sorted_items)
    half_point = length_of_sorted // 2

    if length_of_sorted % 2 != 0:
        return float(sorted_items[half_point])

    first_middle = sorted_items[half_point - 1]
    second_middle = sorted_items[half_point]
    average_middle = (first_middle + second_middle) / 2.0
    return average_middle