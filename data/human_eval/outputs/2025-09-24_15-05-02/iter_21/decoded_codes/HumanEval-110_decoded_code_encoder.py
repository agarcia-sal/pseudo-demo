from typing import List

def exchange(list1: List[int], list2: List[int]) -> str:
    odd = sum(1 for element in list1 if element % 2 == 1)
    even = sum(1 for element in list2 if element % 2 == 0)
    return "YES" if even >= odd else "NO"