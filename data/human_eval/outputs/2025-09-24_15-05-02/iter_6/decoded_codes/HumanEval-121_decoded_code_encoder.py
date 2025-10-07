from typing import List

def solution(list_of_integers: List[int]) -> int:
    sum_of_odd_elements_at_even_positions = 0
    for index in range(len(list_of_integers)):
        element = list_of_integers[index]
        if index % 2 == 0 and element % 2 == 1:
            sum_of_odd_elements_at_even_positions += element
    return sum_of_odd_elements_at_even_positions