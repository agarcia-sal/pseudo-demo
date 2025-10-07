from typing import List, TypeVar

T = TypeVar('T')


def sort_third(list_l: List[T]) -> List[T]:
    list_l = list(list_l)
    indices = range(0, len(list_l), 3)
    sublist_to_sort = [list_l[i] for i in indices]
    sorted_sublist = sorted(sublist_to_sort)
    for idx, val in zip(indices, sorted_sublist):
        list_l[idx] = val
    return list_l