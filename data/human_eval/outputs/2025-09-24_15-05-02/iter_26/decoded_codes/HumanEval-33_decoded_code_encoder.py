from typing import List, TypeVar

T = TypeVar('T')

def sort_third(list_l: List[T]) -> List[T]:
    # Convert input to list if not already a list
    list_l = list(list_l)
    # Extract elements at indices divisible by three
    elements_to_sort = [list_l[i] for i in range(0, len(list_l), 3)]
    # Sort the extracted elements
    sorted_elements = sorted(elements_to_sort)
    # Replace elements at indices divisible by three with the sorted elements
    for idx, val in zip(range(0, len(list_l), 3), sorted_elements):
        list_l[idx] = val
    return list_l