from typing import List

def solution(lst: List[int]) -> int:
    total_sum = 0
    for index in range(len(lst)):
        if index % 2 == 0 and lst[index] % 2 == 1:
            total_sum += lst[index]
    return total_sum