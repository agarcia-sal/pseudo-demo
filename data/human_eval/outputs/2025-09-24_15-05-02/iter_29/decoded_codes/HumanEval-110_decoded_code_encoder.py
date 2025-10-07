from typing import List

def exchange(list_one: List[int], list_two: List[int]) -> str:
    count_odd = sum(1 for element in list_one if element % 2 == 1)
    count_even = sum(1 for element in list_two if element % 2 == 0)
    return "YES" if count_even >= count_odd else "NO"