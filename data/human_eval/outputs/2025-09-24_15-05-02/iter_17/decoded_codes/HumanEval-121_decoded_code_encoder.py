from typing import List

def solution(list_of_integers: List[int]) -> int:
    filtered_list: List[int] = []
    for index, element in enumerate(list_of_integers):
        if index % 2 == 0 and element % 2 == 1:
            filtered_list.append(element)
    result: int = sum(filtered_list)
    return result