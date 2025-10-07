from typing import List

def add(lst: List[int]) -> int:
    total = 0
    index_list = list(range(1, len(lst), 2))
    for i in index_list:
        if lst[i] % 2 == 0:
            total += lst[i]
    return total