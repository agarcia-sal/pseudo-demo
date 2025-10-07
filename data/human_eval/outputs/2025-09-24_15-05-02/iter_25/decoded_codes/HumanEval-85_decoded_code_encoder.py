from typing import List

def add(list_of_integers: List[int]) -> int:
    sum_even_elements_at_odd_indices = 0
    for i in range(1, len(list_of_integers), 2):
        if list_of_integers[i] % 2 == 0:
            sum_even_elements_at_odd_indices += list_of_integers[i]
    return sum_even_elements_at_odd_indices