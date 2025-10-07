from typing import List

def exchange(list_one: List[int], list_two: List[int]) -> str:
    oddCount: int = sum(1 for item in list_one if item % 2 == 1)
    evenCount: int = sum(1 for item in list_two if item % 2 == 0)
    return "YES" if evenCount >= oddCount else "NO"