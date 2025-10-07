from typing import List, Set

def common(l1: List, l2: List) -> List:
    ret: Set = set()
    for e1 in l1:
        for e2 in l2:
            if e1 == e2:
                ret.add(e1)
    return sorted(ret)