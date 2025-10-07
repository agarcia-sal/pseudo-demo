from typing import List

def add(list_of_integers: List[int]) -> int:
    sum_even_elements_at_odd_indices: int = 0
    for index in range(1, len(list_of_integers), 2):
        element = list_of_integers[index]
        if element % 2 == 0:
            sum_even_elements_at_odd_indices += element
    return sum_even_elements_at_odd_indices