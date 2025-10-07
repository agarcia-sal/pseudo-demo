from typing import List

def common(list1: List, list2: List) -> List:
    result_set = set()
    for element1 in list1:
        for element2 in list2:
            if element1 == element2:
                result_set.add(element1)
    return sorted(result_set)