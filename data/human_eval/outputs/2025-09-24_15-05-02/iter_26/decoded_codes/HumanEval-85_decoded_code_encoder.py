from typing import List

def add(list_of_integers: List[int]) -> int:
    return sum(value for i, value in enumerate(list_of_integers) if i % 2 == 1 and value % 2 == 0)