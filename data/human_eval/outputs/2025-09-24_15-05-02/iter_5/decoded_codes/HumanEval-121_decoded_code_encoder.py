from typing import List

def solution(lst: List[int]) -> int:
    filtered_odd_elements = [element for index, element in enumerate(lst) if index % 2 == 0 and element % 2 == 1]
    result = sum(filtered_odd_elements)
    return result