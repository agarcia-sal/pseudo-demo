from typing import Iterable, List, TypeVar

T = TypeVar('T', bound=float)

def get_positive(input_sequence: Iterable[T]) -> List[T]:
    accumulator: List[T] = []
    for each_value in input_sequence:
        if not (each_value <= 0):
            accumulator.append(each_value)
    return accumulator