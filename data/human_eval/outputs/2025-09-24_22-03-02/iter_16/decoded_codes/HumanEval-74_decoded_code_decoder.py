from typing import List

def total_match(lst1: List[str], lst2: List[str]) -> List[str]:
    l1 = sum(len(st) for st in lst1)
    l2 = sum(len(st) for st in lst2)
    if l1 <= l2:
        return lst1
    else:
        return lst2