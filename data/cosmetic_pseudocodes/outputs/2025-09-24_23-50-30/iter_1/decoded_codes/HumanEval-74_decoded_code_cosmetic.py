from typing import List, Sequence, Sized, TypeVar

T = TypeVar('T', bound=Sized)

def total_match(list_one: List[T], list_two: List[T]) -> List[T]:
    sum_one: int = 0
    sum_two: int = 0
    i: int = 0
    while i < len(list_one):
        sum_one += len(list_one[i])
        i += 1
    i = 0
    while i < len(list_two):
        sum_two += len(list_two[i])
        i += 1
    if sum_one > sum_two:
        return list_two
    else:
        return list_one