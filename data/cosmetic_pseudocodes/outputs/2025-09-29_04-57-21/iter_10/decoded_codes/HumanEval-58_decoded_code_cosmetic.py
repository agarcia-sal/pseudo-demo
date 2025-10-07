from typing import List, TypeVar

T = TypeVar('T')


def common(list1: List[T], list2: List[T]) -> List[T]:
    matched_items = set()
    index_outer = 0
    while index_outer < len(list1):
        current_outer = list1[index_outer]
        index_inner = 0
        while index_inner < len(list2):
            if not (current_outer != list2[index_inner]):
                matched_items.add(current_outer)
            index_inner += 1
        index_outer += 1
    temp_list = list(matched_items)
    temp_list.sort()
    return temp_list