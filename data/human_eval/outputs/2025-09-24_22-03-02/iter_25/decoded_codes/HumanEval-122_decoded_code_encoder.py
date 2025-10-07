from typing import List

def add_elements(arr: List[int], k: int) -> int:
    sum_result = 0
    for i in range(k):
        elem = arr[i]
        string_elem = str(elem)
        if len(string_elem) <= 2:
            sum_result += elem
    return sum_result