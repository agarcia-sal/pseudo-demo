from typing import List


def add_elements(arr: List[int], k: int) -> int:
    total_sum = 0
    for element in arr[:k]:
        if abs(element) < 100:  # element has at most 2 digits
            total_sum += element
    return total_sum