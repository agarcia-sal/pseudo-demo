from typing import List

def common(l1: List[int], l2: List[int]) -> List[int]:
    common_elements = set()
    for element1 in l1:
        for element2 in l2:
            if element1 == element2:
                common_elements.add(element1)
    return sorted(common_elements)