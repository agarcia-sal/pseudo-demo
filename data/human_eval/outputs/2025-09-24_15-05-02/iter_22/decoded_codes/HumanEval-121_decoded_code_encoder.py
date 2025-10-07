from typing import List

def solution(list_of_integers: List[int]) -> int:
    sum_of_odd_elements_in_even_positions: int = 0
    for index in range(len(list_of_integers)):
        if index % 2 == 0 and list_of_integers[index] % 2 == 1:
            sum_of_odd_elements_in_even_positions += list_of_integers[index]
    return sum_of_odd_elements_in_even_positions