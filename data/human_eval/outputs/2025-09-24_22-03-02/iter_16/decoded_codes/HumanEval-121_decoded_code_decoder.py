from typing import List

def solution(lst: List[int]) -> int:
    sum_result = 0
    enumerated_list = []
    for idx in range(len(lst)):
        element = lst[idx]
        pair = [idx, element]
        enumerated_list.append(pair)
    for pair in enumerated_list:
        idx = pair[0]
        x = pair[1]
        if idx % 2 == 0 and x % 2 == 1:
            sum_result += x
    return sum_result