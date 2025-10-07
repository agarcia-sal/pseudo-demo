from typing import List

def add(list_of_integers: List[int]) -> int:
    sum_of_selected_elements: int = 0
    for index in range(1, len(list_of_integers), 2):
        if list_of_integers[index] % 2 == 0:
            sum_of_selected_elements += list_of_integers[index]
    return sum_of_selected_elements