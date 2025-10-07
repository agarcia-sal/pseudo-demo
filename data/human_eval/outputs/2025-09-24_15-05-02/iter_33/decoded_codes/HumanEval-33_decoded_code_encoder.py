from typing import List, TypeVar

T = TypeVar('T')

def sort_third(list_l: List[T]) -> List[T]:
    list_l = list(list_l)
    indices = range(0, len(list_l), 3)
    sorted_values = sorted(list_l[i] for i in indices)
    for i, val in zip(indices, sorted_values):
        list_l[i] = val
    return list_l