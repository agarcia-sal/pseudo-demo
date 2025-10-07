from typing import List

def add(list_of_integers: List[int]) -> int:
    if list_of_integers is None:
        raise ValueError("Input list cannot be None")
    return sum(
        value for index, value in enumerate(list_of_integers)
        if index % 2 == 1 and value % 2 == 0
    )