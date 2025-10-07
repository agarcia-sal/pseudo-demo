from typing import List

def solution(lst: List[int]) -> int:
    total_sum: int = 0
    index: int = 0
    while index < len(lst):
        x: int = lst[index]
        remainder_index: int = index % 2
        remainder_x: int = x % 2
        if remainder_index == 0 and remainder_x == 1:
            total_sum += x
        index += 1
    return total_sum