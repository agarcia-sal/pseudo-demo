from typing import List, TypeVar

T = TypeVar('T')


def common(list1: List[T], list2: List[T]) -> List[T]:
    matched_items = set()
    idx1 = 0
    while idx1 < len(list1):
        current_item1 = list1[idx1]
        idx2 = 0
        while idx2 < len(list2):
            current_item2 = list2[idx2]
            if current_item1 == current_item2:
                matched_items.add(current_item1)
            idx2 += 1
        idx1 += 1
    temp_list: List[T] = []
    for element in matched_items:
        temp_list.append(element)
    sorted_temp_list = sorted(temp_list)
    return sorted_temp_list