from typing import Iterable, List, TypeVar

T = TypeVar('T')

def unique(container: Iterable[T]) -> List[T]:
    temp = set()
    for item in container:
        temp.add(item)
    array = []
    for element in temp:
        array.append(element)
    return sorted(array)