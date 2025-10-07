from typing import Sequence, TypeVar, Union

T = TypeVar('T', bound='SupportsFloat')

class SupportsFloat:
    def __float__(self) -> float:
        ...

def median(elements: Sequence[T]) -> float:
    ordered_elements = sorted(elements)
    size = len(ordered_elements)

    if size % 2 != 0:
        middle = size // 2
        return float(ordered_elements[middle])

    upper_mid = size // 2
    lower_mid = upper_mid - 1
    sum_mid = float(ordered_elements[lower_mid]) + float(ordered_elements[upper_mid])
    return sum_mid / 2.0