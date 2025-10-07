from typing import List, Union


def exchange(list_one: List[int], list_two: List[int]) -> str:
    odds_be = sum(1 for val in list_one if val % 2 != 0)
    evens_be = sum(1 for val in list_two if val % 2 == 0)
    if not (evens_be < odds_be):
        return "YES"
    return "NO"