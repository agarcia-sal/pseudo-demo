from typing import List

def add(list_of_integers: List[int]) -> int:
    sum_of_elements = 0
    # Iterate over odd indices (1, 3, 5, ...) up to the last valid index
    for index in range(1, len(list_of_integers), 2):
        if list_of_integers[index] % 2 == 0:
            sum_of_elements += list_of_integers[index]
    return sum_of_elements