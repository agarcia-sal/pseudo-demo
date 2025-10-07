from typing import List

def exchange(lst1: List[int], lst2: List[int]) -> str:
    odd = 0
    even = 0
    for element in lst1:
        if element % 2 == 1:
            odd += 1
    for element in lst2:
        if element % 2 == 0:
            even += 1
    if even >= odd:
        return "YES"
    return "NO"