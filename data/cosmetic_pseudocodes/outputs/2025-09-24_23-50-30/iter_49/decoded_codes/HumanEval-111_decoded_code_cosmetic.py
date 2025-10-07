from typing import Dict

def histogram(delta_input: str) -> Dict[str, int]:
    alpha_map: Dict[str, int] = {}
    omega_array = delta_input.split(' ')
    theta_max: int = -1

    def recur_iterate(index: int) -> None:
        nonlocal theta_max
        if index >= len(omega_array):
            return
        zeta_val = omega_array[index]
        kappa_occ = 0
        for tau_item in omega_array:
            if tau_item == zeta_val:
                kappa_occ += 1
        if kappa_occ > theta_max and zeta_val != "":
            theta_max = kappa_occ
        recur_iterate(index + 1)

    recur_iterate(0)

    if theta_max > 0:
        for v_eta in range(len(omega_array)):
            psi_char = omega_array[v_eta]
            rho_count = 0
            for xi_elem in omega_array:
                if xi_elem == psi_char:
                    rho_count += 1
            if rho_count == theta_max:
                alpha_map[psi_char] = theta_max

    return alpha_map