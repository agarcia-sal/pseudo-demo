from typing import List

def add_elements(arr: List[int], k: int) -> int:
    sum_value = 0
    for index in range(k):
        elem = arr[index]
        elem_str = str(elem)
        elem_length = len(elem_str)
        if elem_length <= 2:
            sum_value += elem
    return sum_value