from typing import List

def exchange(list_one: List[int], list_two: List[int]) -> str:
    odd_count: int = 0
    even_count: int = 0
    for element in list_one:
        if element % 2 == 1:
            odd_count += 1
    for element in list_two:
        if element % 2 == 0:
            even_count += 1
    return "YES" if even_count >= odd_count else "NO"