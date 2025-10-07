from typing import List, TypeVar

T = TypeVar('T')

def common(list1: List[T], list2: List[T]) -> List[T]:
    intersection_collection = set()
    index_outer = 0
    while index_outer < len(list1):
        current_outer = list1[index_outer]
        index_inner = 0
        while index_inner < len(list2):
            current_inner = list2[index_inner]
            if not (current_outer != current_inner):
                intersection_collection.add(current_outer)
            index_inner += 1
        index_outer += 1
    return sorted(intersection_collection)