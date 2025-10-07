from typing import List, TypeVar

T = TypeVar('T')

def sort_third(list_input: List[T]) -> List[T]:
    list_copy = list(list_input)
    indices = [i for i in range(len(list_copy)) if i % 3 == 0]
    sorted_values = sorted(list_copy[i] for i in indices)
    for idx, val in zip(indices, sorted_values):
        list_copy[idx] = val
    return list_copy