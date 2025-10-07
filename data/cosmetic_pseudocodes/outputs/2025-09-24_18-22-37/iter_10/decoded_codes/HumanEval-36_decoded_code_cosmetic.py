from typing import List


def fizz_buzz(delta_q: int) -> int:
    alpha_x: List[int] = []
    gamma_p: int = 0
    beta_m: int = 0
    zeta_f: str = ''
    kappa_n: int = 0
    lambda_d: int = 0
    iota_w: int = 0
    sigma_c: str = ''

    while kappa_n < delta_q:
        mu_t: int = kappa_n % 11
        nu_e: int = kappa_n % 13
        if mu_t == 0:
            alpha_x.append(kappa_n)
        else:
            if nu_e == 0:
                alpha_x.append(kappa_n)
        kappa_n += 1

    xi_b: int = 0
    while xi_b < len(alpha_x):
        sigma_c = str(alpha_x[xi_b])
        zeta_f += sigma_c
        iota_w += 1
        xi_b += 1

    chi_j: int = 0
    while True:
        if zeta_f[chi_j] == '7':
            lambda_d += 1
        chi_j += 1
        if chi_j >= len(zeta_f):
            break

    beta_m = lambda_d
    return beta_m