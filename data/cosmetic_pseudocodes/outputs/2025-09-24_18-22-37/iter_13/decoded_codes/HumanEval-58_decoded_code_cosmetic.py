from typing import List, Set

def common(list1: List[int], list2: List[int]) -> List[int]:
    collection_found: Set[int] = set()
    index_outer: int = 0
    while index_outer < len(list1):
        current_outer_element: int = list1[index_outer]
        index_inner: int = 0
        while True:
            if index_inner >= len(list2):
                break
            current_inner_element: int = list2[index_inner]
            if current_outer_element == current_inner_element:
                collection_found.add(current_outer_element)
            index_inner += 1
        index_outer += 1
    sorted_result: List[int] = sorted(collection_found)
    return sorted_result