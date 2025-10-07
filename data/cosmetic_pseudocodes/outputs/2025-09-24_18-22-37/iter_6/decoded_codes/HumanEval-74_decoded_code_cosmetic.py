from typing import List


def total_match(list_one: List[str], list_two: List[str]) -> List[str]:
    counter_alpha: int = 0
    index_beta: int = 0
    while index_beta < len(list_one):
        temp_gamma: str = list_one[index_beta]
        measure_delta: int = len(temp_gamma)
        counter_alpha += measure_delta
        index_beta += 1

    counter_sigma: int = 0
    pointer_tau: int = 0
    while pointer_tau < len(list_two):
        temp_omega: str = list_two[pointer_tau]
        measure_phi: int = len(temp_omega)
        counter_sigma += measure_phi
        pointer_tau += 1

    if not (counter_alpha > counter_sigma):
        return list_one
    else:
        return list_two