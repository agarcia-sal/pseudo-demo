from typing import List

def total_match(lst1: List[str], lst2: List[str]) -> List[str]:
    l1: int = 0
    for st in lst1:
        l1 += len(st)
    l2: int = 0
    for st in lst2:
        l2 += len(st)
    if l1 <= l2:
        return lst1
    else:
        return lst2