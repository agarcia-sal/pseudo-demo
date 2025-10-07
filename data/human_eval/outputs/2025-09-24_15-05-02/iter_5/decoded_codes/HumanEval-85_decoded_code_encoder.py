from typing import List

def add(lst: List[int]) -> int:
    sum_of_even_elements_at_odd_indices = 0
    for index in range(1, len(lst), 2):
        if lst[index] % 2 == 0:
            sum_of_even_elements_at_odd_indices += lst[index]
    return sum_of_even_elements_at_odd_indices