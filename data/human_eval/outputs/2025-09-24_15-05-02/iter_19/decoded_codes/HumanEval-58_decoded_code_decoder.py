from typing import List, Any

def common(l1: List[Any], l2: List[Any]) -> List[Any]:
    ret = set()
    for element1 in l1:
        for element2 in l2:
            if element1 == element2:
                ret.add(element1)
    result_list = sorted(ret)
    return result_list