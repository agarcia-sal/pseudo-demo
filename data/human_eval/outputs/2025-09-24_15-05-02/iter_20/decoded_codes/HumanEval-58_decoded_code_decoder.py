from typing import List

def common(list1: List[int], list2: List[int]) -> List[int]:
    unique_common_elements = set()
    for element1 in list1:
        for element2 in list2:
            if element1 == element2:
                unique_common_elements.add(element1)
    return sorted(unique_common_elements)