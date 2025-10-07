from typing import Optional, List, TypeVar

T = TypeVar("T")

def next_smallest(lst: List[T]) -> Optional[T]:
    unique_sorted_lst = sorted(set(lst))
    if len(unique_sorted_lst) < 2:
        return None
    else:
        return unique_sorted_lst[1]