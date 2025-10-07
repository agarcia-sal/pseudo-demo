from typing import List, Set

def common(l1: List[str], l2: List[str]) -> List[str]:
    ret: Set[str] = set()
    for e1 in l1:
        for e2 in l2:
            if e1 == e2:
                ret.add(e1)
    return sorted(list(ret))