from typing import Iterable, List, TypeVar

T = TypeVar('T')

def unique(collection: Iterable[T]) -> List[T]:
    temp_set = set()
    iterator = iter(collection)
    while True:
        try:
            element = next(iterator)
            temp_set.add(element)
        except StopIteration:
            break

    temp_list: List[T] = []
    for_element = iter(temp_set)
    counter = 0
    while True:
        try:
            item = next(for_element)
            temp_list.append(item)
            counter += 1
        except StopIteration:
            break

    def compareAscending(a: T, b: T) -> int:
        if a < b:
            return -1
        if a == b:
            return 0
        return 1

    # sort using the comparison function by adapting to key
    # Python's sort() does not support cmp directly, so use key
    from functools import cmp_to_key
    temp_list.sort(key=cmp_to_key(compareAscending))
    return temp_list