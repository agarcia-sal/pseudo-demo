from typing import List

def total_match(lst1: List[str], lst2: List[str]) -> List[str]:
    l1: int = sum(len(st) for st in lst1)
    l2: int = sum(len(st) for st in lst2)
    return lst1 if l1 <= l2 else lst2