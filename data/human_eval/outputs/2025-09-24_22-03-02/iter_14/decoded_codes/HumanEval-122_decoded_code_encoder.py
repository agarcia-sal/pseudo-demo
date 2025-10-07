from typing import List

def add_elements(arr: List[int], k: int) -> int:
    total = 0
    for index in range(min(k, len(arr))):
        elem = arr[index]
        elem_string = str(elem)
        if len(elem_string) <= 2:
            total += elem
    return total