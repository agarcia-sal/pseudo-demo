from typing import List, Optional


def prod_signs(list_alpha: List[int]) -> Optional[int]:
    if len(list_alpha) == 0:
        return None
    list_beta = list_alpha
    flag_has_zero = False
    index_zeta = 0
    max_zeta = len(list_beta) - 1
    while index_zeta <= max_zeta and not flag_has_zero:
        flag_has_zero = (list_beta[index_zeta] == 0) or flag_has_zero
        index_zeta += 1
    scalar_omega = 0
    if not flag_has_zero:
        list_gamma: List[int] = []
        counter_eta = 0
        limit_eta = len(list_beta) - 1
        while counter_eta <= limit_eta:
            element_theta = list_beta[counter_eta]
            if element_theta < 0:
                list_gamma.append(1)
            counter_eta += 1
        scalar_omega = 1
        if len(list_gamma) % 2 == 1:
            scalar_omega = -1
    accumulator_sigma = 0
    dial_iota = 0
    cap_iota = len(list_beta) - 1
    while True:
        accumulator_sigma += abs(list_beta[dial_iota])
        dial_iota += 1
        if dial_iota > cap_iota:
            break
    return scalar_omega * accumulator_sigma