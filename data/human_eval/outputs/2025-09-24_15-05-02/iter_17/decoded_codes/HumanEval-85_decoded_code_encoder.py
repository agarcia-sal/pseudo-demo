from typing import List

def add(lst: List[int]) -> int:
    sum_to_return: int = 0
    for index in range(1, len(lst), 2):
        if lst[index] % 2 == 0:
            sum_to_return += lst[index]
    return sum_to_return