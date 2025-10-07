from typing import List, TypeVar

T = TypeVar('T')

def sort_third(list_of_elements: List[T]) -> List[T]:
    lst = list_of_elements.copy()
    indices = range(0, len(lst), 3)
    elements_at_indices_divisible_by_three = [lst[i] for i in indices]
    sorted_elements = sorted(elements_at_indices_divisible_by_three)
    for i, val in zip(indices, sorted_elements):
        lst[i] = val
    return lst