from typing import Iterable, List, TypeVar

T = TypeVar('T')


def unique(collection_of_items: Iterable[T]) -> List[T]:
    temp_set: set[T] = set()
    index: int = 0
    lst = list(collection_of_items)  # To support indexing

    def accumulate_items(lst: List[T]) -> None:
        nonlocal index
        if index >= len(lst):
            return
        temp_set.add(lst[index])
        index += 1
        accumulate_items(lst)

    accumulate_items(lst)

    temp_list: List[T] = [element for element in temp_set]

    def quicksort(arr: List[T]) -> List[T]:
        if len(arr) <= 1:
            return arr
        pivot = arr[0]
        less = [x for x in arr[1:] if x < pivot]
        greater_eq = [x for x in arr[1:] if not x < pivot]
        return quicksort(less) + [pivot] + quicksort(greater_eq)

    return quicksort(temp_list)