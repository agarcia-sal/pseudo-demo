from typing import List

def add(lst: List[int]) -> int:
    return sum(lst[i] for i in range(1, len(lst), 2) if lst[i] % 2 == 0)