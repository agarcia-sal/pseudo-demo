from typing import List

def exchange(lst1: List[int], lst2: List[int]) -> str:
    odd = sum(i % 2 == 1 for i in lst1)
    even = sum(i % 2 == 0 for i in lst2)
    return "YES" if even >= odd else "NO"