from typing import List

def add(lst: List[int]) -> int:
    sum_even_elements_at_odd_indices: int = 0
    for index in range(1, len(lst), 2):
        if lst[index] % 2 == 0:
            sum_even_elements_at_odd_indices += lst[index]
    return sum_even_elements_at_odd_indices