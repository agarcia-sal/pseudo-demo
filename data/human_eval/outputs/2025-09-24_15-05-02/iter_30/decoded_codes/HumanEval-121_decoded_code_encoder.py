from typing import List

def solution(lst: List[int]) -> int:
    odd_elements_in_even_positions: List[int] = [
        element for index, element in enumerate(lst) if index % 2 == 0 and element % 2 == 1
    ]
    return sum(odd_elements_in_even_positions)