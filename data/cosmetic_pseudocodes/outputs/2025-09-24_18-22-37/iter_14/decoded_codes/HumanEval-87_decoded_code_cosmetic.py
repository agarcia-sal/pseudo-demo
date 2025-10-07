from typing import List, Tuple


def get_row(two_dimensional_list: List[List[int]], target_integer: int) -> List[Tuple[int, int]]:
    epsilon: List[Tuple[int, int]] = []
    sigma = 0
    while sigma < len(two_dimensional_list):
        beta = 0
        current_row = two_dimensional_list[sigma]
        while beta < len(current_row):
            xi = current_row[beta]
            if xi == target_integer:
                epsilon.append((sigma, beta))
            beta += 1
        sigma += 1

    delta = len(epsilon)
    rho = 1
    # Insertion sort on epsilon by row index (ascending)
    while rho < delta:
        kappa = rho
        while kappa > 0 and epsilon[kappa - 1][0] > epsilon[kappa][0]:
            epsilon[kappa], epsilon[kappa - 1] = epsilon[kappa - 1], epsilon[kappa]
            kappa -= 1
        rho += 1

    drip = len(epsilon)
    zeta = 1
    # Insertion sort on epsilon by column index (descending) within same row order
    while zeta < drip:
        psi = zeta
        while psi > 0 and epsilon[psi - 1][1] < epsilon[psi][1]:
            epsilon[psi], epsilon[psi - 1] = epsilon[psi - 1], epsilon[psi]
            psi -= 1
        zeta += 1

    return epsilon