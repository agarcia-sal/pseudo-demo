from typing import List


def solution(list_of_integers: List[int]) -> int:
    if list_of_integers is None:
        raise ValueError("Input list_of_integers must not be None")
    # Sum values that are odd and found at even indices
    return sum(
        value
        for index, value in enumerate(list_of_integers)
        if index % 2 == 0 and value % 2 == 1
    )