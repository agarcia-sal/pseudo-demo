from typing import Sequence, TypeVar, Union

T = TypeVar('T', bound='SupportsFloat')


class SupportsFloat:
    def __float__(self) -> float:
        ...


def median(catalogue: Sequence[T]) -> float:
    sequence = sorted(catalogue)
    length = len(sequence)
    if length == 0:
        raise ValueError("median() arg is an empty sequence")
    if length % 2 == 1:
        midpoint = length // 2
        return float(sequence[midpoint])
    else:
        first_index = (length // 2) - 1
        second_index = length // 2
        sum_of_elements = float(sequence[first_index]) + float(sequence[second_index])
        return sum_of_elements / 2.0