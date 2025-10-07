from typing import List

def add(lst: List[int]) -> int:
    sum_list = [lst[i] for i in range(1, len(lst), 2) if lst[i] % 2 == 0]
    return sum(sum_list)