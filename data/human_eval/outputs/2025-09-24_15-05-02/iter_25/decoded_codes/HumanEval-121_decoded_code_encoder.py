from typing import List

def solution(list_of_integers: List[int]) -> int:
    filtered_list: List[int] = [
        element
        for index, element in enumerate(list_of_integers)
        if index % 2 == 0 and element % 2 == 1
    ]
    result: int = sum(filtered_list)
    return result