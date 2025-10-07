from typing import List

def common(l1: List, l2: List) -> List:
    ret = set()
    for e1 in l1:
        for e2 in l2:
            if e1 == e2:
                ret.add(e1)
    result_list = list(ret)
    sorted_result = sorted(result_list)
    return sorted_result