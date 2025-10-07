from typing import List

def exchange(list_one: List[int], list_two: List[int]) -> str:
    count_of_odd_numbers = sum(1 for x in list_one if x % 2 == 1)
    count_of_even_numbers = sum(1 for x in list_two if x % 2 == 0)
    return "YES" if count_of_even_numbers >= count_of_odd_numbers else "NO"