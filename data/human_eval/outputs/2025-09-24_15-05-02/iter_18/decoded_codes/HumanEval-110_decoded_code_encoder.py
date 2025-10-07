from typing import List

def exchange(lst1: List[int], lst2: List[int]) -> str:
    odd = 0
    for i in lst1:
        if i % 2 == 1:
            odd += 1
    even = 0
    for i in lst2:
        if i % 2 == 0:
            even += 1
    if even >= odd:
        return "YES"
    return "NO"