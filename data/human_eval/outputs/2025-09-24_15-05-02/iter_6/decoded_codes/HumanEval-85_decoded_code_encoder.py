from typing import List

def add(list_of_integers: List[int]) -> int:
    return sum(value for index, value in enumerate(list_of_integers, start=1) if index % 2 == 1 and value % 2 == 0)