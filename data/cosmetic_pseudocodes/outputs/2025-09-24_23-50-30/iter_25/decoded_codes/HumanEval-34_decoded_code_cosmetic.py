from typing import Iterable, List, TypeVar

T = TypeVar('T', bound=object)

def unique(array: Iterable[T]) -> List[T]:
    seen: set[T] = set()
    temp: List[T] = []
    for each_element in array:
        if each_element not in seen:
            temp.append(each_element)
            seen.add(each_element)
    return sorted(temp)