from typing import List, TypeVar, Dict

T = TypeVar('T')

def unique(list_of_elements: List[T]) -> List[T]:
    seen: Dict[T, bool] = {}
    index: int = 0

    def helper_add(elements: List[T]) -> List[T]:
        nonlocal index
        if not (index < len(elements)):
            return []
        seen[elements[index]] = True
        index += 1
        return helper_add(elements)

    helper_add(list_of_elements)

    def helper_filter(keys: List[T]) -> List[T]:
        if len(keys) == 0:
            return []

        def inner_filter(lst: List[T], pos: int) -> List[T]:
            if pos == len(lst):
                return []
            if lst[pos] in seen:
                return [lst[pos]] + inner_filter(lst, pos + 1)
            else:
                return inner_filter(lst, pos + 1)

        return inner_filter(keys, 0)

    keys_list: List[T] = list(seen)
    filtered_keys: List[T] = helper_filter(keys_list)

    return filtered_keys