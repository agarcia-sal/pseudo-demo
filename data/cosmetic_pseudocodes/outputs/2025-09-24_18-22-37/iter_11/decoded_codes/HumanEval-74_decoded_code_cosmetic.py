from typing import List

def total_match(list_one: List[str], list_two: List[str]) -> List[str]:
    counter_alpha: int = 0
    iterator_beta: int = 0
    while iterator_beta < len(list_one):
        temp_gamma: str = list_one[iterator_beta]
        length_delta: int = len(temp_gamma)
        counter_alpha += length_delta
        iterator_beta += 1

    counter_epsilon: int = 0
    iterator_zeta: int = 0
    while iterator_zeta < len(list_two):
        temp_eta: str = list_two[iterator_zeta]
        length_theta: int = len(temp_eta)
        counter_epsilon += length_theta
        iterator_zeta += 1

    if counter_alpha <= counter_epsilon:
        return list_one
    else:
        return list_two