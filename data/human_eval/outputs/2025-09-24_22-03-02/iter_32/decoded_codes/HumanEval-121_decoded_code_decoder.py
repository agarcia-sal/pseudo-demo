from typing import List

def solution(lst: List[int]) -> int:
    sum_result = 0
    index = 0
    while index < len(lst):
        if index % 2 == 0:
            element = lst[index]
            if element % 2 == 1:
                sum_result += element
        index += 1
    return sum_result