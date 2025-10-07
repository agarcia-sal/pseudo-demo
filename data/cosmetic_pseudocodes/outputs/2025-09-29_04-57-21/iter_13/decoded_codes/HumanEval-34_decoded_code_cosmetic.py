from typing import TypeVar, List, Callable

T = TypeVar('T')

def unique(list_of_elements: List[T]) -> List[T]:
    def helper(collection: List[T]) -> List[T]:
        if not collection:
            return []
        head, tail = collection[0], collection[1:]
        filtered_tail = helper([x for x in tail if x != head])
        return [head] + filtered_tail
    temp_unique = helper(list_of_elements)
    return sorted(temp_unique)