from typing import TypeVar, List, Sequence

T = TypeVar('T')

def unique(array_of_items: Sequence[T]) -> List[T]:
    altered_set = set()
    idx = 0
    while idx < len(array_of_items):
        altered_set.add(array_of_items[idx])
        idx += 1
    interim_list: List[T] = []
    iter_idx = 0
    count = len(altered_set)
    altered_list = list(altered_set)
    while iter_idx < count:
        element = altered_list[iter_idx]
        interim_list.append(element)
        iter_idx += 1
    result_list = sorted(interim_list)
    return result_list