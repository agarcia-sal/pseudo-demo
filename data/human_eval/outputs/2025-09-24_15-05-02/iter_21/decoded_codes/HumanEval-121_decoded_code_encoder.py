from typing import List

def solution(list_of_integers: List[int]) -> int:
    filtered_elements: List[int] = []
    for index in range(len(list_of_integers)):
        element = list_of_integers[index]
        if index % 2 == 0 and element % 2 == 1:
            filtered_elements.append(element)
    result = sum(filtered_elements)
    return result