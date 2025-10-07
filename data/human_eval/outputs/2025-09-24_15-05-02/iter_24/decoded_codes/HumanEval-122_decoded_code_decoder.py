from typing import List

def add_elements(arr: List[int], k: int) -> int:
    total_sum = 0
    for element in arr[:k]:
        if len(str(element)) <= 2:
            total_sum += element
    return total_sum