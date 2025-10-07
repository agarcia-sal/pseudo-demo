from typing import List, Sequence, TypeVar

T = TypeVar('T')

def total_match(list_one: Sequence[T], list_two: Sequence[T]) -> Sequence[T]:
    len_one: int = sum(len(e) for e in list_one)
    len_two: int = sum(len(f) for f in list_two)
    result: Sequence[T] = list_two if len_one > len_two else list_one
    return result