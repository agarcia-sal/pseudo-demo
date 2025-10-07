from typing import List

def add_elements(list_of_integers: List[int], integer_k: int) -> int:
    sum_total: int = 0
    # Sum elements from index 0 up to integer_k (excluded) with string length <= 2
    for element in list_of_integers[:integer_k]:
        if len(str(element)) <= 2:
            sum_total += element
    return sum_total