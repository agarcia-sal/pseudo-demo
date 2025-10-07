from typing import List

def add_elements(arr: List[int], k: int) -> int:
    return sum(element for element in arr[:k] if len(str(element)) <= 2)