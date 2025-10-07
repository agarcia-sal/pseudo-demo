from typing import List

def add_elements(arr: List[int], k: int) -> int:
    return sum(elem for elem in arr[:k] if len(str(elem)) <= 2)