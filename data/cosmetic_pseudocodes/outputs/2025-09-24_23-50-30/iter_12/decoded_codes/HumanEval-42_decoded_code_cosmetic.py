from typing import Sequence, List, TypeVar

T = TypeVar('T', bound=int)

def incr_list(collection: Sequence[T]) -> List[int]:
    result: List[int] = []
    index: int = 0
    while index < len(collection):
        result.append(collection[index] + 1)
        index += 1
    return result