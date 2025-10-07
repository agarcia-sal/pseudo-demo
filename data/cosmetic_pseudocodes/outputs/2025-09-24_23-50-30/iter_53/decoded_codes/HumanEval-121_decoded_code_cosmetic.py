from typing import List

def solution(value_list: List[int]) -> int:
    acc: int = 0
    pos: int = 0
    while pos < len(value_list):
        if (pos % 2 == 0) and (value_list[pos] % 2 == 1):
            acc += value_list[pos]
        pos += 1
    return acc