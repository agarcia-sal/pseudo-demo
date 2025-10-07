from typing import List

def add_elements(arr: List[int], k: int) -> int:
    sum_result = 0
    for element in arr[:k]:
        if len(str(element)) <= 2:
            sum_result += element
    return sum_result