from typing import List, Sequence, TypeVar

T = TypeVar('T', bound=Sequence)

def total_match(list_one: List[T], list_two: List[T]) -> List[T]:
    acc_a: int = 0
    for elem_a in list_one:
        acc_a += len(elem_a)
    acc_b: int = 0
    for elem_b in list_two:
        acc_b += len(elem_b)
    if not (acc_b < acc_a):
        return list_one
    else:
        return list_two