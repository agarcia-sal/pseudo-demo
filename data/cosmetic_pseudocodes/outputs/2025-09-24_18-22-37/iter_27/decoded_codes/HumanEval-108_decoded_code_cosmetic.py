from typing import List

def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        omega: int = 1
        if integer_value < 0:
            integer_value = -integer_value
            omega = -1
        zeta: str = str(integer_value)
        delta_list: List[int] = []
        idx_gamma: int = 0
        while idx_gamma < len(zeta):
            char_val: str = zeta[idx_gamma]
            int_val: int = int(char_val)
            delta_list.append(int_val)
            idx_gamma += 1
        delta_list[0] = delta_list[0] * omega
        summation: int = 0
        idx_eta: int = 0
        while idx_eta < len(delta_list):
            summation += delta_list[idx_eta]
            idx_eta += 1
        return summation

    psi: List[int] = []
    iter_tau: int = 0
    while iter_tau < len(array_of_integers):
        item_phi: int = array_of_integers[iter_tau]
        val_theta: int = digits_sum(item_phi)
        psi.append(val_theta)
        iter_tau += 1

    sigma: List[int] = []
    pos_iota: int = 0
    while pos_iota < len(psi):
        elem_kappa: int = psi[pos_iota]
        if elem_kappa <= 0:
            pos_iota += 1
            continue
        else:
            sigma.append(elem_kappa)
        pos_iota += 1

    return len(sigma)