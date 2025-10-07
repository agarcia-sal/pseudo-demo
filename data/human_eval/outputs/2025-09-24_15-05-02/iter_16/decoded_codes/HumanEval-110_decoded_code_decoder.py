from typing import List

def exchange(list1: List[int], list2: List[int]) -> str:
    odd_count: int = 0
    even_count: int = 0

    for element in list1:
        if element % 2 == 1:
            odd_count += 1

    for element in list2:
        if element % 2 == 0:
            even_count += 1

    if even_count >= odd_count:
        return "YES"
    else:
        return "NO"