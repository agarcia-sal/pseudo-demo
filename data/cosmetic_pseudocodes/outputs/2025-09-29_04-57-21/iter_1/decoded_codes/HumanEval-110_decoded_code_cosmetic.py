from typing import List

def exchange(list_one: List[int], list_two: List[int]) -> str:
    odds: int = sum(1 for value in list_one if value % 2 == 1)
    evens: int = sum(1 for item in list_two if item % 2 == 0)
    return "YES" if evens >= odds else "NO"