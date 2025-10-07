from typing import List, TypeVar

T = TypeVar('T', bound='object')

def common(list1: List[T], list2: List[T]) -> List[T]:
    unique_collection: set[T] = set()
    index_outer: int = 0
    while index_outer < len(list1):
        current_outer = list1[index_outer]
        index_inner: int = 0
        while index_inner < len(list2):
            current_inner = list2[index_inner]
            if current_outer == current_inner:
                unique_collection.add(current_outer)
                index_inner = len(list2)  # exit inner loop
            else:
                index_inner += 1
        index_outer += 1
    sorted_collection: List[T] = [item for item in unique_collection]
    sorted_collection.sort()
    return sorted_collection