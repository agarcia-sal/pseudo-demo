from typing import Iterable, List, TypeVar

T = TypeVar('T')

def unique(seq: Iterable[T]) -> List[T]:
    temp_set: set[T] = set()
    temp_list: list[T] = []
    for elem in seq:
        if elem not in temp_set:
            temp_list.append(elem)
            temp_set.add(elem)
    return sorted(temp_list)