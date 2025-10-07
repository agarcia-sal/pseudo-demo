from typing import List

def common(list1: List[int], list2: List[int]) -> List[int]:
    ret = set()
    for element1 in list1:
        for element2 in list2:
            if element1 == element2:
                ret.add(element1)
    return sorted(ret)