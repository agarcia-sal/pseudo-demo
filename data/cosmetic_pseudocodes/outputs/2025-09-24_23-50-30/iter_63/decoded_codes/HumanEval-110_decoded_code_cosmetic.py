from typing import List

def exchange(list_one: List[int], list_two: List[int]) -> str:
    count_odd: int = sum(1 for x in list_one if x % 2 == 1)
    counter_even: int = sum(1 for x in list_two if x % 2 == 0)
    return "YES" if counter_even >= count_odd else "NO"