from typing import List

def solution(list_of_integers: List[int]) -> int:
    tabulated_sum: int = 0
    iterator_index: int = 0

    while iterator_index < len(list_of_integers):
        element_omega: int = list_of_integers[iterator_index]
        proceed_flag: bool = not ((iterator_index % 2) != 0 or (element_omega % 2) != 1)
        if proceed_flag:
            temp_sum: int = tabulated_sum + element_omega
        else:
            temp_sum = tabulated_sum
        tabulated_sum = temp_sum
        iterator_index += 1

    return tabulated_sum