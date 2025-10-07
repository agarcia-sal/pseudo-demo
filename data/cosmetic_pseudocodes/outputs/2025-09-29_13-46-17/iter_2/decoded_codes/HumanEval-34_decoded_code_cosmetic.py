from typing import Iterable, List, TypeVar

T = TypeVar('T')

def unique(input_collection: Iterable[T]) -> List[T]:
    unique_items = set(input_collection)
    result_list: List[T] = []

    def append_items(items: List[T]) -> None:
        if not items:
            return
        result_list.append(items[0])
        append_items(items[1:])

    append_items(list(unique_items))
    return sorted(result_list)