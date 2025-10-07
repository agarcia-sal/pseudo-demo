from typing import Iterable, List, Sequence, TypeVar

T = TypeVar('T', bound=int)

def incr_list(collection: Sequence[T]) -> List[int]:
    new_list: List[int] = []
    iterator: int = 0
    while iterator < len(collection):
        value: int = collection[iterator]
        new_list.append(1 + value)
        iterator += 1
    return new_list