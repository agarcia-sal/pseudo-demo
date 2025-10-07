from typing import List

def add(lst: List[int]) -> int:
    return sum(x for x in lst[1:len(lst):2] if x % 2 == 0)