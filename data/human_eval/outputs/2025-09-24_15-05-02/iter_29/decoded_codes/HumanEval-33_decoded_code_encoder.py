from typing import List, TypeVar

T = TypeVar('T')

def sort_third(list_l: List[T]) -> List[T]:
    list_l = list_l.copy()
    indices = range(0, len(list_l), 3)
    elements_at_indices_divisible_by_three = [list_l[i] for i in indices]
    sorted_elements = sorted(elements_at_indices_divisible_by_three)
    for idx, val in zip(indices, sorted_elements):
        list_l[idx] = val
    return list_l