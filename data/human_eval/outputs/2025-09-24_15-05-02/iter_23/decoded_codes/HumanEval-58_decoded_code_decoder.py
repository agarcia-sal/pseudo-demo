from typing import List

def common(list1: List[int], list2: List[int]) -> List[int]:
    result_set = set()
    for element1 in list1:
        for element2 in list2:
            if element1 == element2:
                result_set.add(element1)
    result_list = sorted(result_set)
    return result_list