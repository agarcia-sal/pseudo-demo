from typing import List

def solution(lst: List[int]) -> int:
    total = 0
    index = 0
    while index < len(lst):
        element = lst[index]
        if index % 2 == 0 and element % 2 == 1:
            total += element
        index += 1
    return total