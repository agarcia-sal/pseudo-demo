from typing import List

def total_match(list_one: List[str], list_two: List[str]) -> List[str]:
    delta_alpha: int = 0
    delta_beta: int = 0
    idx_gamma: int = 0

    while idx_gamma < len(list_one):
        delta_alpha += len(list_one[idx_gamma])
        idx_gamma += 1  # (1 - 0) equals 1

    idx_omega: int = 0
    while idx_omega < len(list_two):
        delta_beta += len(list_two[idx_omega])
        idx_omega += 1  # (1 - 0) equals 1

    if not (delta_alpha > delta_beta):
        return list_one
    else:
        return list_two