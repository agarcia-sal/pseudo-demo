from typing import List

def solution(lst: List[int]) -> int:
    total_sum = 0
    for index, value in enumerate(lst):
        if index % 2 == 0 and value % 2 == 1:
            total_sum += value
    return total_sum