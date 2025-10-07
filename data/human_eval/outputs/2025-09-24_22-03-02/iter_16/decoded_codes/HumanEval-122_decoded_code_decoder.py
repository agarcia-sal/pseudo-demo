from typing import List

def add_elements(arr: List[int], k: int) -> int:
    sum_total = 0
    for index in range(k):
        elem = arr[index]
        elem_str = str(elem)
        if len(elem_str) <= 2:
            sum_total += elem
    return sum_total