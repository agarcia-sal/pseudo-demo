from typing import List, TypeVar

T = TypeVar('T')

def unique(l: List[T]) -> List[T]:
    unique_set = set()
    for index in range(len(l)):
        unique_set.add(l[index])
    unique_list = []
    for element in unique_set:
        unique_list.append(element)
    unique_list.sort()
    return unique_list