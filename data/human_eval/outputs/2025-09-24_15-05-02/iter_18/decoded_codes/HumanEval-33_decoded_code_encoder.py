from typing import List, TypeVar

T = TypeVar('T')

def sort_third(l: List[T]) -> List[T]:
    l_copy = l.copy()
    indices = range(0, len(l_copy), 3)
    sorted_elements = sorted(l_copy[i] for i in indices)
    for idx, val in zip(indices, sorted_elements):
        l_copy[idx] = val
    return l_copy