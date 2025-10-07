from typing import List

def solution(lst: List[int]) -> int:
    result = 0
    index = 0
    while index < len(lst):
        x = lst[index]
        if index % 2 == 0 and x % 2 == 1:
            result += x
        index += 1
    return result