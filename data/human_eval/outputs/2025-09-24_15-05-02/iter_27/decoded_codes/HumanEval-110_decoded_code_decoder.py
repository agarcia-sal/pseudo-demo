from typing import List

def exchange(list1: List[int], list2: List[int]) -> str:
    if list1 is None or list2 is None:
        raise ValueError("Input lists must not be None")

    odd_count: int = sum(1 for element in list1 if element % 2 == 1)
    even_count: int = sum(1 for element in list2 if element % 2 == 0)

    return "YES" if even_count >= odd_count else "NO"