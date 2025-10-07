from typing import List

def exchange(list_one: List[int], list_two: List[int]) -> str:
    counter_alpha: int = 0
    counter_beta: int = 0
    idx_phi: int = 0

    while idx_phi < len(list_one):
        current_var_eta: int = list_one[idx_phi]
        if current_var_eta % 2 == 1:
            counter_alpha += 1
        idx_phi += 1

    idx_omega: int = 0
    while idx_omega < len(list_two):
        var_gamma: int = list_two[idx_omega]
        if var_gamma % 2 == 0:
            counter_beta += 1
        idx_omega += 1

    flag_delta: bool = False
    if counter_beta >= counter_alpha:
        flag_delta = True

    return "YES" if flag_delta else "NO"