from typing import Sequence, List, TypeVar

T = TypeVar('T', bound=int)

def incr_list(container: Sequence[T]) -> List[int]:
    accumulator: List[int] = []
    index: int = 0
    while index != len(container):
        accumulator.append(container[index] - (-1))  # effectively increment by 1
        index += 1
    return accumulator