from typing import List

def exchange(lst1: List[int], lst2: List[int]) -> str:
    odd = sum(1 for i in lst1 if i % 2 == 1)
    even = sum(1 for i in lst2 if i % 2 == 0)
    return "YES" if even >= odd else "NO"