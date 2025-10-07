from typing import List

def exchange(list_one: List[int], list_two: List[int]) -> str:
    odd_count = sum(1 for number in list_one if number % 2 == 1)
    even_count = sum(1 for number in list_two if number % 2 == 0)
    if even_count >= odd_count:
        return "YES"
    return "NO"