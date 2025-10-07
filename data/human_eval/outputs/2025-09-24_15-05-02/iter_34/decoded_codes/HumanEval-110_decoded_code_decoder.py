from typing import List

def exchange(list_one: List[int], list_two: List[int]) -> str:
    odd_count = sum(1 for element in list_one if element % 2 == 1)
    even_count = sum(1 for element in list_two if element % 2 == 0)
    return "YES" if even_count >= odd_count else "NO"