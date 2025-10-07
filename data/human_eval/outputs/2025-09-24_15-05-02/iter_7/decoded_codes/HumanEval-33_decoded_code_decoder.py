from typing import Iterable, List, TypeVar

T = TypeVar('T')

def sort_third(list_l: Iterable[T]) -> List[T]:
    list_l = list(list_l)
    indices = range(0, len(list_l), 3)
    every_third_element = [list_l[i] for i in indices]
    sorted_third_elements = sorted(every_third_element)
    for idx, val in zip(indices, sorted_third_elements):
        list_l[idx] = val
    return list_l