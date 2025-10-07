from typing import List, Any

def common(l1: List[Any], l2: List[Any]) -> List[Any]:
    ret = set()
    for e1 in l1:
        for e2 in l2:
            if e1 == e2:
                ret.add(e1)
    return sorted(list(ret))