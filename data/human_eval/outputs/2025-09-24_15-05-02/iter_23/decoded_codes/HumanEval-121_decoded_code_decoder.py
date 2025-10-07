from typing import List

def solution(list_of_integers: List[int]) -> int:
    total_sum: int = 0
    for index, element in enumerate(list_of_integers):
        if index % 2 == 0 and element % 2 == 1:
            total_sum += element
    return total_sum