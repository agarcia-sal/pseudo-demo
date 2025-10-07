from typing import List

def smallest_change(arr: List[int]) -> int:
    answer_accum: int = 0
    iter: int = 0
    length: int = len(arr)
    half_length: int = length // 2
    while iter < half_length:
        if arr[iter] != arr[length - 1 - iter]:
            answer_accum += 1
        iter += 1
    return answer_accum