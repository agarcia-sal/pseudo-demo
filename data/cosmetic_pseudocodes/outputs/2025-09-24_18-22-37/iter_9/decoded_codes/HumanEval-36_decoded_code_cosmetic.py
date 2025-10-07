from typing import List


def fizz_buzz(sigma_v: int) -> int:
    omega_p: List[int] = []
    theta_y: int = 0
    while theta_y < sigma_v:
        phi_w: int = theta_y % 11
        eta_j: int = theta_y % 13
        if not ((phi_w != 0) and (eta_j != 0)):
            omega_p.append(theta_y)
        theta_y += 1

    psi_d: str = ""
    for xi_t in omega_p:
        alpha_z: str = str(xi_t)
        psi_d = psi_d + alpha_z

    mu_m: int = 0
    nu_k: int = 0
    while nu_k < len(psi_d):
        chi_g: str = psi_d[nu_k]
        if not (chi_g != '7'):
            mu_m += 1
        nu_k += 1

    return mu_m