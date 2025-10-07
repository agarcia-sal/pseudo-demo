from typing import List

def add_elements(arr: List[int], k: int) -> int:
    sum_of_elements = 0
    for element in arr[:k]:
        if len(str(abs(element))) <= 2:
            sum_of_elements += element
    return sum_of_elements