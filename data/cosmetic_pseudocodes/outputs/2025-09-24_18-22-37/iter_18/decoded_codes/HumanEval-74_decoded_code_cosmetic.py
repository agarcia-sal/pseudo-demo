from typing import List, Sequence

def total_match(list_one: Sequence[str], list_two: Sequence[str]) -> Sequence[str]:
    sum_length_alpha: int = 0
    sum_length_beta: int = 0
    iterator_omega: int = 0
    while iterator_omega < len(list_one):
        current_element_sigma: str = list_one[iterator_omega]
        temp_length_theta: int = len(current_element_sigma)
        sum_length_alpha += temp_length_theta
        iterator_omega += 1
    iterator_phi: int = 0
    while True:
        current_element_delta: str = list_two[iterator_phi]
        temp_length_gamma: int = len(current_element_delta)
        sum_length_beta += temp_length_gamma
        iterator_phi += 1
        if iterator_phi >= len(list_two):
            break
    if not (sum_length_alpha > sum_length_beta):
        return list_one
    else:
        return list_two