from typing import List

def solution(list_of_integers: List[int]) -> int:
    total: int = 0
    for index in range(len(list_of_integers)):
        current_element = list_of_integers[index]
        if (index % 2 == 0) and (current_element % 2 == 1):
            total += current_element
    return total