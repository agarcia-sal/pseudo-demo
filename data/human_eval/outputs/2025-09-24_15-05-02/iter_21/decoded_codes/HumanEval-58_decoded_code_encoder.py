from typing import List

def common(list1: List[int], list2: List[int]) -> List[int]:
    result = set()
    for element1 in list1:
        for element2 in list2:
            if element1 == element2:
                result.add(element1)
    sorted_result = sorted(result)
    return sorted_result