from typing import Sequence, List, TypeVar

T = TypeVar('T', bound=int)

def incr_list(collection: Sequence[T]) -> List[int]:
    result: List[int] = []
    for index in range(len(collection)):
        result.append(collection[index] - (-1))
    return result