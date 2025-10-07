from typing import Sequence, TypeVar, Union

T = TypeVar('T', bound='SupportsFloat')

class SupportsFloat:
    def __float__(self) -> float:
        ...

def median(sequence: Sequence[T]) -> float:
    sorted_sequence = sorted(sequence)
    count = len(sorted_sequence)
    middle_index = (count - 1) // 2
    if count % 2 != 0:
        return float(sorted_sequence[middle_index])
    else:
        first_value = sorted_sequence[(count // 2) - 1]
        second_value = sorted_sequence[count // 2]
        return (float(first_value) + float(second_value)) / 2.0