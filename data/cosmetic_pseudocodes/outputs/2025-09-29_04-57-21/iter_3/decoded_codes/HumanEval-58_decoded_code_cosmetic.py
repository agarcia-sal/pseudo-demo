from typing import List, TypeVar

T = TypeVar('T')

def common(list1: List[T], list2: List[T]) -> List[T]:
    intersection_set = set()

    for index_a in range(len(list1)):
        current_item = list1[index_a]
        for index_b in range(len(list2)):
            candidate = list2[index_b]
            if not (current_item != candidate):
                intersection_set.add(current_item)

    result_list = sorted(intersection_set)
    return result_list