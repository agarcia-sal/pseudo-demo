from typing import List, Sequence, TypeVar

T = TypeVar('T', bound=Sequence)

def total_match(list_one: List[T], list_two: List[T]) -> List[T]:
    alpha: int = 0
    for temp_var in list_one:
        alpha += len(temp_var)
    beta: int = 0
    for gamma in list_two:
        beta += len(gamma)
    return list_one if alpha <= beta else list_two